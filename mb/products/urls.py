from django.conf.urls import include, url

from products.views import ItemListView, ItemView


urlpatterns = [
    url(r'^items/$', ItemListView.as_view(), name='item-list'),
    url('^item/(?P<pk>[\w-]+)$', ItemView.as_view(), name='item-detail'),
]