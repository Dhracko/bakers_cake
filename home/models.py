"""Define the structure of stored data"""

from django.db import models


class NewsletterEmail(models.Model):
    """Defines email fields"""
    contact_email = models.EmailField(max_length=254, null=False, blank=True)

    def __str__(self):
        return self.contact_email
