from siteapi.models import Story
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
