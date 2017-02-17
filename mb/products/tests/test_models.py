
from django.test import TestCase
from django.utils import timezone

from datetime import datetime
from products.models  import Item, ItemCategory, ItemType

from django.utils.crypto import get_random_string
from decimal import Decimal
from random import randint


def create_item_type(*args, **kwargs):
    defaults = {
        'type_num': int(get_random_string(4, '1234567890')),
        'type_name': get_random_string(4, 'abcdefgh')
    }
    defaults.update(kwargs)
    item_type = ItemType.objects.create(**defaults)
    return item_type


def create_item_category(*args, **kwargs):
    defaults = {
        'category': int(get_random_string(4, '1234567890')),
        'cat_name': get_random_string(4, 'abcdefgh')
    }
    defaults.update(kwargs)
    item_cat = ItemCategory.objects.create(**defaults)
    return item_cat


def create_item(*args, **kwargs):
    defaults = {
        'sku': int(get_random_string(4, '1234567890')),
        'upc': get_random_string(4, 'ABCDEFGH'),
        'price': Decimal(randint(5, 100)),
        'stock_qty': int(get_random_string(4, '1234567890')),
        'name': get_random_string(6, 'ABCDefg'),
        'active': 1,
        'available': True,
        'vintage': get_random_string(4, 'ABCDEFGH'),
        'created': datetime.now(),
        'size_value': get_random_string(4, 'ABCDEFGH'),
    }
    defaults.update(kwargs)
    item = Item.objects.create(**defaults)
    return item


# models test
class ItemModelTest(TestCase):

    def test_item_type_creation(self):
        item_type = create_item_type(type_name='23OZ')
        self.assertTrue(ItemType.objects.get(pk=item_type.pk).type_name == '23OZ')

    def test_item_category_creation(self):
        item_cat = create_item_category(cat_name='23OZ')
        self.assertTrue(ItemCategory.objects.get(pk=item_cat.pk).cat_name == '23OZ')

    def test_item_creation(self):
        item_cat = create_item_category(cat_name='23OZ')
        item_type = create_item_type(type_name='23OZ')
        item = create_item(category=item_cat, type_num=item_type)
        self.assertIsInstance(Item.objects.get(pk=item.pk), Item)
