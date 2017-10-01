from siteapi.models import Character
from siteapi.mixins.json import JSONDetailView, JSONListView, JSONCreateView, JSONUpdateView, \
    JSONDeleteView, PermissionRequiredJSONMixin


class CharacterDetail(PermissionRequiredJSONMixin, JSONDetailView):
    model = Character
    context_object_name = 'character'
    permission_required = 'siteapi.character_detail'


class CharacterList(PermissionRequiredJSONMixin, JSONListView):
    model = Character
    context_object_name = 'characters'
    permission_required = 'siteapi.character_list'
    paginate_by = 10

    def get_queryset(self):
        if 'world_pk' in self.kwargs:
            return self.model.objects.filter(world_id=self.kwargs['world_pk'])
        return super(CharacterList, self).get_queryset()


class CharacterCreate(PermissionRequiredJSONMixin, JSONCreateView):
    model = Character
    context_object_name = 'character'
    permission_required = 'siteapi.character_create'
    fields = Character.editable_fields
    sluggable = True
    ownable = True


class CharacterUpdate(PermissionRequiredJSONMixin, JSONUpdateView):
    model = Character
    context_object_name = 'character'
    permission_required = 'siteapi.character_update'
    fields = Character.editable_fields
    sluggable = True
    ownable = True


class CharacterDelete(PermissionRequiredJSONMixin, JSONDeleteView):
    model = Character
    permission_required = 'siteapi.character_delete'
