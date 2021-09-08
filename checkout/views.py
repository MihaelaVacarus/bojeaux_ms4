from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JCSsRFn0PukwazQBeDExUUsj22W2mMI1V6bcvg8fgVXIyv0r7jdRYjBytADgMLVLdiYBWucNOCwV10R3NWrOySN003FbUxDK1',
    }

    return render(request, template, context)
