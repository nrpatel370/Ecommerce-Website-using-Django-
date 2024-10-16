from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Value, F
from django.db.models.aggregates import Count
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('<10', "Low")
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)
    
    
# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse('admin:store_product_changelist') + '?' + urlencode({'collection__id': str(collection.id)})
        return format_html('<a href = {}>{}</a>', url, collection.products_count)
   
    
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(products_count= Count('products'))

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    autocomplete_fields = ['product']
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_status', 'customer_name']
    list_select_related = ['customer']
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    def customer_name(self, order):
        return order.customer


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {
        'slug': ['title']
    }
    autocomplete_fields = ['collection']
    actions = ['clearInventory']
    list_display = ['title', 'unit_price', 'inventory_status' , 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_select_related = ['collection']
    search_fields = ['orders']

    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'low'
        
        return 'ok'

    def collection_title(self, product):
        return product.collection.title


    @admin.action(description="Clear Inventory")
    def clearInventory(self, req, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(req, f"{updated_count} products were updated")

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    
    list_display = ['first_name', 'last_name', 'membership', 'customer_order']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['customer', 'first_name__istartswith', "last_name__istartswith"]
    def customer_order(self, customer):
        return customer.customer_order
    
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(customer_order= Count(F('order__customer_id')))

