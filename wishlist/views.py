from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import UserProfile, Product, Wishlist


@login_required
def wishlist(request):
    """ A view to return the wishlist or create one if none yet """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user_profile=profile)
    wishlist_products = Product.objects.filter(wishlist__user_profile=profile)

    context = {
        'profile': profile,
        'wishlist_products': wishlist_products,
    }
    return render(request, "wishlist/wishlist.html", context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add products to wishlist"""

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user_profile=user)

    if product in wishlist.products.all():
        messages.info(
            request, f'You have already added {product.name} to your wishlist!')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} added to wishlist!')
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """ A view to remove products from the wishlist"""

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist = get_object_or_404(Wishlist, user_profile=user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(
            request, f'{product.name} removed from your wishlist.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, f'{product.name} is not on your wishlist!')
        return redirect(request.META.get('HTTP_REFERER'))

