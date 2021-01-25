"""Display the models in the admin panel"""


from django.contrib import admin
from .models import NewsletterEmail


admin.site.register(NewsletterEmail)
