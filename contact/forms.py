from django import forms


class ContactForm(forms.Form):
    """
    Creates the fields in the contact form.
    arg: contact_name
        contact_email
        context as textarea
    """
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
