from django import forms
from django.core.exceptions import ValidationError

from products.models import Item


class ItemSearchForm(forms.Form):

    sku = forms.CharField(
        label="Item Sku",
        required=False,
    )

    description = forms.CharField(
        label="Item Description",
        required=False,
    )

    name = forms.CharField(
        label="Item Name",
        required=False,
    )


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['sku', 'name']
