"""
 Forms Module
"""
from django import forms
from .models import ContactEmail


class EmailForm(forms.ModelForm):
    """
    Base for Email Newsletter Form
    tasks with common behaviors: extends forms.ModelForm
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """ Recall the models """
        model = ContactEmail
        fields = ['contact_email']
