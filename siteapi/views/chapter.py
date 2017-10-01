from siteapi.models import Chapter
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class ChapterDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = Chapter
    context_object_name = 'chapter'
    permission_required = 'siteapi.chapter_detail'


class ChapterList(PermissionRequiredJSONMixin, JSONListView):
    model = Chapter
    context_object_name = 'chapters'
    permission_required = 'siteapi.chapter_list'
    paginate_by = 10


class ChapterCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = Chapter
    context_object_name = 'chapter'
    permission_required = 'siteapi.chapter_create'
    fields = Chapter.editable_fields
    sluggable = True
    ownable = True


class ChapterUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = Chapter
    context_object_name = 'chapter'
    permission_required = 'siteapi.chapter_update'
    fields = Chapter.editable_fields
    sluggable = True
    ownable = True


class ChapterDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = Chapter
    permission_required = 'siteapi.chapter_delete'
