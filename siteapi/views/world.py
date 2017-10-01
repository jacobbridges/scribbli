from siteapi.models import World
from siteapi.mixins.json import JSONCreateView, JSONUpdateView, JSONDetailView, JSONListView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class WorldDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = World
    context_object_name = 'world'
    permission_required = 'siteapi.world_detail'


class WorldList(PermissionRequiredJSONMixin, JSONListView):
    model = World
    context_object_name = 'worlds'
    permission_required = 'siteapi.world_list'
    paginate_by = 10

    def get_queryset(self):
        if 'universe_pk' in self.kwargs:
            return self.model.objects.filter(universe_id=self.kwargs['universe_pk'])
        return super(WorldList, self).get_queryset()


class WorldCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = World
    context_object_name = 'world'
    permission_required = 'siteapi.world_create'
    fields = World.editable_fields
    sluggable = True
    ownable = True


class WorldUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = World
    context_object_name = 'world'
    permission_required = 'siteapi.world_update'
    fields = World.editable_fields
    sluggable = True
    ownable = True


class WorldDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = World
    permission_required = 'siteapi.world_delete'
