from . models import Coffee
from django import forms

class CoffeeEntry(forms.Form):
    producer = forms.CharField(max_length=50, required=True)
    region = forms.CharField(max_length=50, required=True)
    variety = forms.CharField(max_length=50, required=True)
    process = forms.CharField(max_length=50, required=True)
    flavournotes = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = Coffee

