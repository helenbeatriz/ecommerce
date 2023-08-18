from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    basket = request.session.get('basket', {}) 
    
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment") 
        return redirect('products')  # You can use the view name directly

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            # Save the order form data and process the order
            order = order_form.save()
            # Perform other order processing tasks
            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_success')  # Redirect to a success page
    else:
        order_form = OrderForm()
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NgYEQGETKbO2ZE5YsXJUNVYwFVgQV1fX8FIntiAxl92EAPCRjE9g9VJ7EGD0gW3fjJtJ5C0UCXaVKhw0nFflWFc00ZtgaXf5u',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
