from siteapi.models import UploadedImage
from siteapi.mixins.json import JSONCreateView, JSONUpdateView, JSONDetailView, JSONListView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class ImageDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = UploadedImage
    context_object_name = 'image'
    permission_required = 'siteapi.image_detail'


class ImageList(PermissionRequiredJSONMixin, JSONListView):
    model = UploadedImage
    context_object_name = 'images'
    permission_required = 'siteapi.image_list'
    paginate_by = 10


class ImageCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = UploadedImage
    context_object_name = 'image'
    permission_required = 'siteapi.image_create'
    fields = UploadedImage.editable_fields
    ownable = True


class ImageUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = UploadedImage
    context_object_name = 'image'
    permission_required = 'siteapi.image_update'
    fields = UploadedImage.editable_fields
    ownable = True


class ImageDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = UploadedImage
    permission_required = 'siteapi.image_delete'
