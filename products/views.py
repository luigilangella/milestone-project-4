from django.shortcuts import render, get_object_or_404
from .models import Product, Preference
from django.contrib.auth.decorators import login_required

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

@login_required
def productpreference(request, product_id, userpreference):
    products = Product.objects.all()
    if request.method == "POST":
        eachproduct = get_object_or_404(Product, id=product_id)
        

        obj = ''

        valueobj = ''

        try:
            obj = Preference.objects.get(user=request.user, product=eachproduct)

            valueobj = obj.value  # value of userpreference

            valueobj = int(valueobj)

            userpreference = int(userpreference)

            if valueobj != userpreference:
                obj.delete()

                upref = Preference()
                upref.user = request.user

                upref.product = eachproduct

                upref.value = userpreference

                if userpreference == 1 and valueobj != 1:
                    eachproduct.likes += 1
                    eachproduct.dislikes -= 1
                elif userpreference == 2 and valueobj != 2:
                    eachproduct.dislikes += 1
                    eachproduct.likes -= 1

                upref.save()

                eachproduct.save()

                return render(request, 'products.html', {'products':products})

            elif valueobj == userpreference:
                obj.delete()

                if userpreference == 1:
                    eachproduct.likes -= 1
                elif userpreference == 2:
                    eachproduct.dislikes -= 1

                eachproduct.save()


                return render(request, 'products.html', {'products':products})

        except Preference.DoesNotExist:
            upref = Preference()

            upref.user = request.user

            upref.product = eachproduct

            upref.value = userpreference

            userpreference = int(userpreference)

            if userpreference == 1:
                eachproduct.likes += 1
            elif userpreference == 2:
                eachproduct.dislikes += 1

            upref.save()

            eachproduct.save()

            return render(request, 'products.html', {'products':products})

    else:
        
        return render(request, 'products.html', {'products':products})