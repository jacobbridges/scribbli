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


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs.update(dict(ensure_ascii=False))
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
                serialize_context[key] = obj.values()
            else:
                serialize_context[key] = obj
        return dict(success=True, data=serialize_context)

    def make_error(self, error, status_code=400, **extra):
        """
        Return the error as a JSON response.
        """
        data = dict(success=False, data=dict(message=error, **extra))
        return self.render_to_json_response(data, status_code=status_code)


class JSONCreateView(JSONResponseMixin, BaseCreateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONDetailView(JSONResponseMixin, BaseDetailView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONUpdateView(JSONResponseMixin, BaseUpdateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONListView(JSONResponseMixin, BaseListView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class JSONDeleteView(JSONResponseMixin, BaseDeleteView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
