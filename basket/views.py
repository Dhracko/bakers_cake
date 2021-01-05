from django.shortcuts import render


def view_basket(request):
    """ A view to return basket page """
    return render(request, 'basket/basket.html')
