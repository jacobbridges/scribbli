class Serializable(object):
    def serialize(self): return {}


class SerializeRelatedObjectsMixin(Serializable):
    serialize_relations = False

    def serialize(self):
        if not self.serialize_relations:
            return super(SerializeRelatedObjectsMixin, self).serialize()
        data = super(SerializeRelatedObjectsMixin, self).serialize()
        related_objects = []
        for obj in self._meta.related_objects:
            relation = obj.get_accessor_name()
            try:
                relation_list = getattr(self, relation).all().values_list('pk', flat=True)
            except:
                relation_list = []
            related_objects.append({
                'model': obj.related_model.__name__,
                'relation': relation,
                'list': relation_list,
            })
        data.update({
            'related_objects': related_objects
        })
        return data

