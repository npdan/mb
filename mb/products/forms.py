from django import forms
from django.core.exceptions import ValidationError

from products.models import Item


class ItemSearchForm(forms.Form):

    sku = forms.CharField(
        label="Item Sku",
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search by Sku', 'class':'form-control'})
    )

    name = forms.CharField(
        label="Item Name",
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search by Name', 'class': 'form-control'})
    )

    '''
    description = forms.CharField(
        label="Item Description",
        required=False,
    )
    '''


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'upc', 'price', 'stock_qty',
            'name', 'active', 'available', 'vintage',
            'created', 'size_value', 'category', 'type_num',
        ]
