from django.shortcuts import render
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.utils.http import urlencode
from django.core.urlresolvers import reverse_lazy

from products.models import Item
from products.forms import ItemForm, ItemSearchForm


class ItemListView(ListView):

    context_object_name = "items"
    template_name = "item_list.html"
    paginate_by = 30

    def get_queryset(self):
        get = self.request.GET.copy()
        if(len(get)):
            get.pop('page', None)
        self.baseurl = urlencode(get)
        self.form = ItemSearchForm(self.request.GET)
        if self.form.is_valid():
            filters = Item.get_queryset(self.form.cleaned_data)
            if len(filters):
                query = Item.objects.filter(filters)
            else:
                query = Item.objects.all()
        return query

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['baseurl']= self.baseurl
        return context


class ItemView(UpdateView):
    context_object_name = 'item'
    template_name = "item_detail.html"
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('products:item-list')
    # success_url = 'items'
