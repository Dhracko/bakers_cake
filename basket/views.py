"""Web request and returns a Web response for basket"""

from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ A view that returns basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified cake to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name}\
             quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{basket[item_id]} x {product.name}\
              has been added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified cake in the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name}\
             quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'{product.name} has been from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove the cake from the shopping basket """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
