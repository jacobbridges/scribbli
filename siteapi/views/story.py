from siteapi.models import Story, StoryTag
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class StoryDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = Story
    context_object_name = 'story'
    permission_required = 'siteapi.story_detail'


class StoryList(PermissionRequiredJSONMixin, JSONListView):
    model = Story
    context_object_name = 'stories'
    permission_required = 'siteapi.story_list'
    paginate_by = 10


class StoryCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = Story
    context_object_name = 'story'
    permission_required = 'siteapi.story_create'
    fields = Story.editable_fields
    sluggable = True
    ownable = True


class StoryUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = Story
    context_object_name = 'story'
    permission_required = 'siteapi.story_update'
    fields = Story.editable_fields
    sluggable = True
    ownable = True


class StoryDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = Story
    permission_required = 'siteapi.story_delete'


class StoryAddTag(JSONUpdateView):
    model = Story
    context_object_name = 'story'
    fields = []

    def form_valid(self, form):
        response = super(StoryAddTag, self).form_valid(form)
        try:
            tag = StoryTag.objects.get(pk=self.kwargs['tag_pk'])
        except StoryTag.DoesNotExist:
            return self.throw_error(
                'No story_tag exists with pk of {}'.format(self.kwargs['tag_pk']), status_code=404)
        self.object.tags.add(tag)
        self.object.save()
        if hasattr(self, 'context_object_name'):
            data = dict()
            data[self.context_object_name] = self.object
        else:
            data = dict(object=self.object)
        return self.render_to_json_response(data)
