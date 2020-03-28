from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Preference, CatalogCategory, Catalog, ProductDetail, ProductAttribute
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


def shop(request):
    return render(request, 'shop.html')

def wines(request):
    products = Product.objects.all().filter(category__name='Wine')
    print(products)
    return render(request, 'wines.html', {'products':products})

def dairy(request):
    products = Product.objects.all().filter(category__name='Dairy')
    print(products)
    return render(request, 'dairy.html', {'products':products})

def cured_meats(request):
    products = Product.objects.all().filter(category__name='Cured Meats')
    print(products)
    return render(request, 'cured_meats.html', {'products':products})

def fruit_and_veg(request):
    products = Product.objects.all().filter(category__name='Fruit and Veg')
    print(products)
    return render(request, 'fruit_and_veg.html', {'products':products})

def fish_fresh(request):
    products = Product.objects.all().filter(category__name="Fish and Seafood").filter(details__value='fresh')
    print(products)
    return render(request, 'fish_fresh.html', {'products':products})

def fish_frozen(request):
    products = Product.objects.all().filter(category__name="Fish and Seafood").filter(details__value='frozen')
    print(products)
    return render(request, 'fish_frozen.html', {'products':products})

def dry_store(request):
    products = Product.objects.all().filter(category__name="Dry Store")
    print(products)
    return render(request, 'dry_store.html', {'products':products})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

@login_required
def productpreference(request, product_id, userpreference):
    products = Product.objects.all()
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        obj = ''
        valueobj = ''
        try:
            obj = Preference.objects.get(user=request.user, product=product) 
            valueobj = obj.value  # value of userpreference
            valueobj = int(valueobj)
            userpreference = int(userpreference)
            if valueobj != userpreference:
                obj.delete()
                upref = Preference()
                upref.user = request.user
                upref.product = product
                upref.value = userpreference
                if userpreference == 1 :
                    product.likes += 1
                    product.dislikes -= 1
                elif userpreference == 2:
                    product.dislikes += 1
                    product.likes -= 1
                upref.save()
                product.save()
                data = { 'id':product.id, 'likes': product.likes, 'dislikes': product.dislikes }
                return JsonResponse(data)
            elif valueobj == userpreference:
                obj.delete()

                if userpreference == 1:
                    product.likes -= 1
                elif userpreference == 2:
                    product.dislikes -= 1

                product.save()
                data = {'id':product.id, 'likes': product.likes, 'dislikes': product.dislikes }
                return JsonResponse(data) 
                
        except Preference.DoesNotExist:
            upref = Preference()
            upref.user = request.user
            upref.product = product
            upref.value = userpreference
            userpreference = int(userpreference)
            if userpreference == 1:
                product.likes += 1
            elif userpreference == 2:
                product.dislikes += 1
            upref.save()
            product.save()
            data = { 'id':product.id,'likes': product.likes, 'dislikes': product.dislikes }
            return JsonResponse(data)
            
    else:
        data = serializers.serialize('json', products)
        return JsonResponse({'products':data})
        