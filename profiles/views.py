from django.shortcuts import render,redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile.
    arg: profile
     """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Profile updated \
                                                        successfully')
        else:
            messages.error(request, 'Sorry, there was a problem \
                            updating the profile right now.\
                            Please try again later.')
            return redirect(reverse('profile'))

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
