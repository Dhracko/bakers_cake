"""
Views Module
"""

from django.shortcuts import render, redirect
from .models import NewsletterEmail


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def add_news(request):
    """Create an item into the newsletter module
    using the method POST"""

    if request.method == 'POST':
        news_email = request.POST.get('contact_email')
        NewsletterEmail.objects.create(contact_email=news_email)

        return redirect('home')

    return render(request, 'home/index.html')
