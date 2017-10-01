from siteapi.models import Destination
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class DestinationDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = Destination
    context_object_name = 'destination'
    permission_required = 'siteapi.destination_detail'


class DestinationList(PermissionRequiredJSONMixin, JSONListView):
    model = Destination
    context_object_name = 'destinations'
    permission_required = 'siteapi.destination_list'
    paginate_by = 10

    def get_queryset(self):
        if 'world_pk' in self.kwargs:
            return self.model.objects.filter(world_id=self.kwargs['world_pk'])
        return super(DestinationList, self).get_queryset()


class DestinationCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = Destination
    context_object_name = 'destination'
    permission_required = 'siteapi.destination_create'
    fields = Destination.editable_fields
    sluggable = True
    ownable = True


class DestinationUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = Destination
    context_object_name = 'destination'
    permission_required = 'siteapi.destination_update'
    fields = Destination.editable_fields
    sluggable = True
    ownable = True


class DestinationDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = Destination
    permission_required = 'siteapi.destination_delete'
