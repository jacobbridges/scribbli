from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound, Http404
from django.utils.text import slugify
from rules.contrib.views import PermissionRequiredMixin

from django.http import JsonResponse
from django.db.models.base import ModelBase
from django.db.models.query import QuerySet
from django.db.models.fields.related import ManyToManyField
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView, BaseUpdateView, BaseDeleteView
from django.views.generic.list import BaseListView


def model_to_dict(instance):
    """
    Convert a django model to a Python dictionary.
    """
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data


class ShortCircuitHttpChain(Exception):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.get('response', None)
        super(ShortCircuitHttpChain, self).__init__(*args)


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(JSONResponseMixin, self).dispatch(request, *args, **kwargs)
        except ShortCircuitHttpChain as short_circuit:
            return short_circuit.response

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs.update(dict(json_dumps_params=dict(ensure_ascii=False)))
        return JsonResponse(self.safe_json(context), **response_kwargs)

    def safe_json(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        serialize_context = dict()
        for key, obj in context.items():
            if isinstance(obj.__class__, ModelBase):
                if hasattr(obj, 'serialize') and callable(getattr(obj, 'serialize')):
                    serialize_context[key] = obj.serialize()
                else:
                    serialize_context[key] = model_to_dict(obj)
            elif isinstance(obj, QuerySet):
                serialize_context[key] = [o.serialize() for o in obj if hasattr(o, 'serialize')]
                if len(serialize_context[key]) != len(obj):
                    serialize_context[key] = [model_to_dict(o) for o in obj]
            elif key == 'extra':
                serialize_context[key] = obj
            # elif key == 'view':
            #     continue
            # else:
            #     serialize_context[key] = obj
        return dict(success=True, data=serialize_context)

    def make_error(self, error, status_code=400, raise_=True, **extra):
        """
        Return the error as a JSON response.
        """
        data = dict(success=False, data=dict(message=error, **extra))
        if raise_:
            raise ShortCircuitHttpChain(response=JsonResponse(data, status=status_code))
        else:
            return JsonResponse(data, status=status_code)


class JSONResponseSingleObjectMixin(JSONResponseMixin):

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(JSONResponseSingleObjectMixin, self).dispatch(request, *args, **kwargs)
        except Http404 as response:
            return self.make_error(response.__str__(), status_code=404, raise_=False)


class JSONCreateView(JSONResponseSingleObjectMixin, BaseCreateView):
    sluggable = False

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('POST')

    def get_form_kwargs(self):
        if not all(x in self.request.POST for x in self.fields):
            return self.make_error('All fields are required.', required_fields=self.fields)
        return super(JSONCreateView, self).get_form_kwargs()

    def form_valid(self, form):
        response = super(JSONCreateView, self).form_valid(form)
        if self.sluggable:
            setattr(
                self.object,
                'slug',
                slugify(getattr(
                    self.object,
                    self.model.sluggable_field), allow_unicode=True))
            self.object.save()
        if hasattr(self, 'context_object_name'):
            data = dict()
            data[self.context_object_name] = self.object
        else:
            data = dict(object=self.object)
        return self.render_to_json_response(data)

    def form_invalid(self, form):
        response = super(JSONCreateView, self).form_invalid(form)
        return self.make_error('Data failed validation.', **form.errors)

    def get_success_url(self):
        return ''


class JSONDetailView(JSONResponseSingleObjectMixin, BaseDetailView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONUpdateView(JSONResponseSingleObjectMixin, BaseUpdateView):
    sluggable = False

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('POST')

    def get_form_kwargs(self):
        if not all(x in self.request.POST for x in self.fields):
            return self.make_error('All fields are required.', required_fields=self.fields)
        return super(JSONUpdateView, self).get_form_kwargs()

    def form_valid(self, form):
        response = super(JSONUpdateView, self).form_valid(form)
        if self.sluggable:
            setattr(
                self.object,
                'slug',
                slugify(getattr(
                    self.object,
                    self.model.sluggable_field), allow_unicode=True))
            self.object.save()
        if hasattr(self, 'context_object_name'):
            data = dict()
            data[self.context_object_name] = self.object
        else:
            data = dict(object=self.object)
        return self.render_to_json_response(data)

    def form_invalid(self, form):
        response = super(JSONUpdateView, self).form_invalid(form)
        return self.make_error('Data failed validation.', **form.errors)

    def get_success_url(self):
        return ''


class JSONListView(JSONResponseMixin, BaseListView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONDeleteView(JSONResponseSingleObjectMixin, BaseDeleteView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('DELETE')

    def get_success_url(self):
        return ''


class PermissionRequiredJSONMixin(JSONResponseMixin, PermissionRequiredMixin):
    def handle_no_permission(self):
        return self.make_error('Permission denied.', status_code=403)
