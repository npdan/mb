from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse

from products.views  import ItemListView
from test_models import create_item_type, create_item_category, create_item


# models test
class ItemListViewTest(TestCase):

    def setUp(self):
        item_cat = create_item_category(cat_name='23OZ')
        item_type = create_item_type(type_name='23OZ')
        self.item = create_item(category=item_cat, type_num=item_type)
        self.factory = RequestFactory()

    def test_item_list_view(self):
        url = reverse('products:item-list')
        request = self.factory.get(url)
        request.user = AnonymousUser()
        response = ItemListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_item_view(self):
        url = reverse('products:item-detail', args={'pk': self.item.pk})
        request = self.factory.get(url)
        request.user = AnonymousUser()
        response = ItemListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
