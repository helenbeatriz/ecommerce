from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    basket = request.session.get("basket", {})
    basket_items = []
    total = Decimal(0)
    product_count = 0

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        item_total = product.price * quantity
        total += item_total
        product_count += quantity
        basket_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
                "item_total": item_total,
            }
        )

    delivery = Decimal(0)
    free_delivery_delta = Decimal(0)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    grand_total = delivery + total

    context = {
        "basket_items": basket_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
