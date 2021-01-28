"""Web request and returns a Web response for contact"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the admin with the
            # contact information
            template = get_template('contact/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage("New contact form submission", content,
                                 "Bakers Cake" + '',
                                 ['bakerscake.web@gmail.com'],
                                 headers={'Reply-To': contact_email}
                                 )
            email.send()
            messages.success(request, 'Thank you for contact us, We will reply to\
                your query as soon as we can.')
            return redirect('home')

    return render(request, 'contact/contact.html', {'form': form_class, })
