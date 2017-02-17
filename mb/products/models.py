from __future__ import unicode_literals

import datetime
from datetime import datetime
from collections import OrderedDict
from django.contrib import admin
from django.db import models
from django.core.urlresolvers import reverse

from utils import FKXMLImporter
from data_importer.importers import XMLImporter


ACTIVE_CHOICES = (
    (1, 'Active'),
    (2, 'Inactive'),
    (3, 'Maybe'),
)


class Item(models.Model):
    sku = models.PositiveIntegerField(primary_key=True)
    upc = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')
    stock_qty = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=256, default='')
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES, default=1)
    available = models.BooleanField(default=False)
    vintage = models.CharField(max_length=256, default='', blank=True)
    created = models.DateTimeField(max_length=256, default=datetime.now)
    size_value = models.CharField(max_length=256)
    category = models.ForeignKey('ItemCategory')
    type_num = models.ForeignKey('ItemType')

    @staticmethod
    def get_queryset(params):
        sku = params.get('sku')
        name = params.get('name')
        qset = models.Q(pk__gt = 0)
        if sku:
            qset &= models.Q(sku__icontains=sku)
        if name:
            qset &= models.Q(name__icontains=name)
        return qset

    def get_absolute_url(self):
        return reverse('item-detail', pk=[str(self.pk)])

    def __unicode__(self):
        return u'%s: %s' % (self.sku, self.name)


class ItemCategory(models.Model):
    category = models.PositiveIntegerField(primary_key=True)
    cat_name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % (self.cat_name)


class ItemType(models.Model):
    type_num = models.PositiveIntegerField(primary_key=True)
    type_name = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % (self.type_name)


class ItemAdmin(admin.ModelAdmin):
    pass


class ItemCategoryAdmin(admin.ModelAdmin):
    pass


class ItemTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemType, ItemTypeAdmin)


class ItemXMLImporterModel(FKXMLImporter):
    fields = OrderedDict((
        ('sku', 0),
        ('upc', 1),
        ('price', 2),
        ('stock_qty', 3),
        ('name', 4),
        ('active', 5),
        ('available', 6),
        ('vintage', 7),
        ('created', 8),
        ('size_value', 9),
        ('category_id', 10),
        ('type_num_id', 12),
    ))
    root = 'item'

    class Meta:
        model = Item


class ItemCategoryXMLImporterModel(XMLImporter):
    fields = OrderedDict((
        ('category', 10),
        ('cat_name', 11)
    ))
    root = 'item'
    class Meta:
        model = ItemCategory

class ItemTypeXMLImporterModel(XMLImporter):
    fields = OrderedDict((
        ('type_num', 12),
        ('type_name', 13)
    ))
    root = 'item'
    class Meta:
        model = ItemType


def do_import(source):
    errors = []
    categories = ItemCategoryXMLImporterModel(source=source.name)
    categories.save()
    if categories.errors:
        errors.append(categories.errors)
    types = ItemTypeXMLImporterModel(source=source.name)
    types.save()
    if types.errors:
        errors.append(types.errors)
    items = ItemXMLImporterModel(source=source.name)
    items.save()
    if items.errors:
        errors.append(items.errors)
    return errors