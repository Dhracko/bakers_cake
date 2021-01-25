from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors.keys())
        self.assertEqual(form.errors['contact_email'][0],
                         'This field is required.')

    def test_contact_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_name', form.errors.keys())
        self.assertEqual(form.errors['contact_name'][0], 'This field is required.')

    def test_content_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
