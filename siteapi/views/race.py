from siteapi.models import Race
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class RaceDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = Race
    context_object_name = 'race'
    permission_required = 'siteapi.race_detail'


class RaceList(PermissionRequiredJSONMixin, JSONListView):
    model = Race
    context_object_name = 'races'
    permission_required = 'siteapi.race_list'
    paginate_by = 10


class RaceCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = Race
    context_object_name = 'race'
    permission_required = 'siteapi.race_create'
    fields = Race.editable_fields
    sluggable = True
    ownable = True


class RaceUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = Race
    context_object_name = 'race'
    permission_required = 'siteapi.race_update'
    fields = Race.editable_fields
    sluggable = True
    ownable = True


class RaceDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = Race
    permission_required = 'siteapi.race_delete'
