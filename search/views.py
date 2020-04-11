from django.shortcuts import render
from products.models import Product

def do_search(request):
    """ A simple view to provide the user with a search box to find a specific product. """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
