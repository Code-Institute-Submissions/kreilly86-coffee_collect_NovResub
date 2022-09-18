from django import forms
from . models import Coffee


class CoffeeEntry(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('producer', 'region', 'variety', 'process', 'flavournotes',)
