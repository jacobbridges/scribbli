from django.forms import ModelForm

from siteapi.models import World


class WorldForm(ModelForm):

    class Meta:
        model = World
        fields = ['name', 'description', 'is_public', 'universe']
