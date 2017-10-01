from siteapi.models import StoryPost
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class StoryPostDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = StoryPost
    context_object_name = 'story_post'
    permission_required = 'siteapi.story_post_detail'


class StoryPostList(PermissionRequiredJSONMixin, JSONListView):
    model = StoryPost
    context_object_name = 'story_posts'
    permission_required = 'siteapi.story_post_list'
    paginate_by = 10


class StoryPostCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = StoryPost
    context_object_name = 'story_post'
    permission_required = 'siteapi.story_post_create'
    fields = StoryPost.editable_fields
    sluggable = True
    ownable = True


class StoryPostUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = StoryPost
    context_object_name = 'story_post'
    permission_required = 'siteapi.story_post_update'
    fields = StoryPost.editable_fields
    sluggable = True
    ownable = True


class StoryPostDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = StoryPost
    permission_required = 'siteapi.story_post_delete'
