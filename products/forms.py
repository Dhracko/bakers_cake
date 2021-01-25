""" Forms for products"""

from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from products.models import Review, RATE_CHOICES


class ProductForm(forms.ModelForm):
    """
    Create a form for product management
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded'


class RateForm(forms.ModelForm):
    """ Create a form for Rate """
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'exampleFormControlTextarea1', 'rows': "3"}), required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Review
        fields = ('text', 'rate')
