from django import forms
from .models import Item


class CreateForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['delivery', 'safe_sale']
