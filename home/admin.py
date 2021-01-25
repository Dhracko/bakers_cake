"""
Admin Module
Use to register the models
"""


from django.contrib import admin
from .models import NewsletterEmail


admin.site.register(NewsletterEmail)
