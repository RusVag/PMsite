from django.contrib import admin
from .models import *
# Register your models here.
class ItemInCollInline(admin.StackedInline):
    model = ItemInCollections
    extra = 0

class CollectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Collection._meta.fields]
    inlines = [ItemInCollInline]
    prepopulated_fields = {'slug':('name',),}

    class Meta:
        model = Collection
    
    
admin.site.register(Collection, CollectionAdmin)


class ItemInCollsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ItemInCollections._meta.fields]

    class Meta:
        model = ItemInCollections

admin.site.register(ItemInCollections, ItemInCollsAdmin)