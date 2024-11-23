from django.contrib import admin
from .models import *
from catalog.models import ClothItem
# Register your models here.

# admin.site.register(Status)
# admin.site.register(ProductInOrder)
# admin.site.register(Order)


# admin.site.register(Status)

class ProductInOrderInline(admin.StackedInline):
    model = ProductInOrder
    extra = 0

class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'customer__id', "customer__first_name", "customer__last_name", 'total_price', 'status__name', 'created', 'updated']
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order
    # list_display = ['id', 'customer__username', "customer__first_name", "customer__last_name", 'status__name', "total_price", 'created', 'updated']
    
admin.site.register(Order, OrderAdmin)



class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = ['order__id', 'item__name', 'count', 'is_active', 'price_per_item', 'total_price']

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)