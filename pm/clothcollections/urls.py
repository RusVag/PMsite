from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='colls'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', CollInfo, name='details'),
    # path('add/', addItem, name='add'),
    # path('collections/', Collections, name='collections'),
    # path('type/<slug:cat_slug>/', index, name='category'),
]
