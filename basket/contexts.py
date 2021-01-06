from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    # free_delivery_collection = settings.FREE_DELIVERY_COLLECTION

    # Calculate the cost of delivery and it's free if it past the threshold
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        # 'free_delivery_collection': settings.FREE_DELIVERY_COLLECTION,
        'grand_total': grand_total,
    }

    return context
