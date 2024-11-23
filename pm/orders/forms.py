from .models import *
from django.forms import *
from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class CheckoutContactForm(forms.Form):
    address = forms.CharField(required=True)
    phone = PhoneNumberField(required=True)

