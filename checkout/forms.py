""" Forms for checkout """

from django import forms
from .models import Order
from django.forms import TextInput


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode',
                  'county', 'phone_number',)
        widgets = {
            'phone_number': TextInput(attrs={'type': 'tel',
                                             'pattern': '[0-9]{11}'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'street_address1': 'First line Address',
            'street_address2': 'Second Line Address',
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
            'county': 'County',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
