from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='basket'

urlpatterns = [
    path('', basket_adding, name='basket_adding'),
    path('checkout/', checkout, name='checkout'),


]