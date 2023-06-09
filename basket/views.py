from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

def view_basket(request):
    """ A view that renders the basket contents page """
    basket = request.session.get('basket', {})
    basket_items = []

    for item_id, quantity in basket.items():
        product = Product.objects.get(pk=item_id)
        basket_items.append({
            'product': product,
            'quantity': quantity,
        })

    context = {
        'basket_items': basket_items,
    }
    return render(request, 'basket/basket.html', context)


def move_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(pk=item_id)

    basket = request.session.get('basket', {})
    basket[item_id] = basket.get(item_id, 0) + quantity

    request.session['basket'] = basket

    messages.success(request, f'{quantity} {product.name}(s) added to the basket.')
    return redirect(redirect_url)
