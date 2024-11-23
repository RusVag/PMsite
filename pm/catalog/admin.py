from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(TypeOfClothing)
# admin.site.register(ClothItem)
class CatAdmin(admin.ModelAdmin):
    list_display = ['kindName', 'id']
    search_fields = ['kindName', 'id']
    prepopulated_fields = {'slug':('kindName',),}

admin.site.register(KindOfClothing, CatAdmin)
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeName__kind', 'typeName__typeName', 'price', 'id']
    search_fields = ['name', 'typeName__kind', 'typeName__typeName']
    
    prepopulated_fields = {'slug':('name',),}
admin.site.register(ClothItem, ItemAdmin)




