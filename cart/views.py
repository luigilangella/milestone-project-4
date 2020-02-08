from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect

def view_cart(request):
    """
        A view that renders the carts contents page
    """
    return render(request, 'cart.html')

def add_to_cart(request, id):
    """
        Add a quantity to the specified product to the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    request.session['cart'] = cart
    
    return redirect(reverse('index'))

def adjust_cart(request, id):
    """
        Adjust a quantity to the specified product of the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))
