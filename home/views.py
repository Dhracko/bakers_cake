"""Web request and returns a Web response for home"""


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterEmail


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def add_news(request):
    """Create an email into the newsletter module
    using the method POST"""

    if request.method == 'POST':
        news_email = request.POST.get('contact_email')
        NewsletterEmail.objects.create(contact_email=news_email)
        messages.success(request, 'Thank you for joining our newsletter!!')
        return redirect('home')

    return render(request, 'home/index.html')
