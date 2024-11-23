from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='catalog'

urlpatterns = [
    path('', index, name='index'),
    path('add/', addItem, name='add'),
    path('type/<slug:cat_slug>/', index, name='category'),
    # path('<slug:slug>/', ItemDetail.as_view(), name='details'),
    # path('<int:product_id>/', product, name='details'),
    path('<slug:slug>/', ItemInfo, name='details'),
]
