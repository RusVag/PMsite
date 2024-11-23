from .models import *
from django.forms import *
from django import forms

class AddItemForm(ModelForm):
    class Meta:
        model = ClothItem
        fields = ['frontpic', 'backpic', 'name', 'price', 'typeName', 'size_choice', 'description']

        widgets = {
            'description':forms.Textarea(attrs={'class':'form-input',
                                                'rows':6, 'cols':100, 'style': 'font-size: 1.2rem; font-weight: bold',
                                                'white-space':'pre-wrap',})
        }


class ShowItemForm(ModelForm):
    class Meta:
        model = ClothItem
        fields = ['frontpic', 'backpic', 'name', 'price', 'typeName', 'description']


