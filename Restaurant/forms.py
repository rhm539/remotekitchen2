# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Menu, MenuItem

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'description']

MenuItemFormSet = inlineformset_factory(Menu, MenuItem, form=MenuItemForm, extra=1)
