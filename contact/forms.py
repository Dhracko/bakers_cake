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

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Your name:',
            'contact_email': 'Your email:',
            'content': 'What would you like to tell us?',
        }

        self.fields['contact_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-blue rounded contact-form'
            self.fields[field].label = False
