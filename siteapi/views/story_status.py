from siteapi.models import StoryStatus
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class StoryStatusDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = StoryStatus
    context_object_name = 'story_status'
    permission_required = 'siteapi.story_status_detail'


class StoryStatusList(PermissionRequiredJSONMixin, JSONListView):
    model = StoryStatus
    context_object_name = 'story_statuss'
    permission_required = 'siteapi.story_status_list'
    paginate_by = 10


class StoryStatusCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = StoryStatus
    context_object_name = 'story_status'
    permission_required = 'siteapi.story_status_create'
    fields = StoryStatus.editable_fields
    sluggable = True
    ownable = True


class StoryStatusUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = StoryStatus
    context_object_name = 'story_status'
    permission_required = 'siteapi.story_status_update'
    fields = StoryStatus.editable_fields
    sluggable = True
    ownable = True


class StoryStatusDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = StoryStatus
    permission_required = 'siteapi.story_status_delete'