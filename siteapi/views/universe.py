from siteapi.models import Universe
from siteapi.mixins.json import JSONCreateView, JSONUpdateView, JSONDetailView, JSONListView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class UniverseDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = Universe
    context_object_name = 'universe'
    permission_required = 'siteapi.universe_detail'


class UniverseList(PermissionRequiredJSONMixin, JSONListView):
    model = Universe
    context_object_name = 'universes'
    permission_required = 'siteapi.universe_list'
    paginate_by = 10


class UniverseCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = Universe
    context_object_name = 'universe'
    permission_required = 'siteapi.universe_create'
    fields = Universe.editable_fields
    sluggable = True


class UniverseUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = Universe
    context_object_name = 'universe'
    permission_required = 'siteapi.universe_update'
    fields = Universe.editable_fields
    sluggable = True


class UniverseDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = Universe
    permission_required = 'siteapi.universe_delete'
