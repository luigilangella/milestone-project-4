from django.test import TestCase
from .views import shop
from django.shortcuts import render, get_object_or_404
from .models import Product, Preference, CatalogCategory, Catalog, ProductDetail, ProductAttribute, User



class TestShopView(TestCase):
    """ A series of tests to make sure all the views of the products app render as expected. """
    def test_that_the_shop_view_renders(self):

        page = self.client.get('/shop')
        self.assertEqual(page.status_code, 200)

    def test_that_the_wines_view_renders(self):
        products = Product.objects.all().filter(category__name='Wine')
        page = self.client.get('/products/wines/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_dairy_view_renders(self):
        products = Product.objects.all().filter(category__name='Dairy')
        page = self.client.get('/products/dairy/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_cured_meats_view_renders(self):
        products = Product.objects.all().filter(category__name='Cured Meats')
        page = self.client.get('/products/cured_meats/',
                               {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_fruit_and_veg_view_renders(self):
        products = Product.objects.all().filter(category__name='Fruit and Veg')
        page = self.client.get(
            '/products/fruit_and_veg/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_fresh_fish_view_renders(self):
        products = Product.objects.all().filter(
            category__name="Fish and Seafood").filter(details__value='fresh')
        page = self.client.get('/products/fish_fresh/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_frozen_fish_view_renders(self):
        products = Product.objects.all().filter(
            category__name="Fish and Seafood").filter(details__value='frozen')
        page = self.client.get('/products/fish_frozen/',
                               {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_dry_store_view_renders(self):
        products = Product.objects.all().filter(category__name='Dry Store')
        page = self.client.get('/products/dry_store/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_all_products_view_renders(self):
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_the_product_preference_1_view(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99')
        product.save()
        preference = Preference(value='1', user=user, product=product)
        preference.save()
        response = self.client.post('/products/{0}/preference/{1}/'.format(product.id,preference.value),follow=True)
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)
    
    def test_the_product_preference_2_view(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99')
        product.save()
        preference = Preference(value='2', user=user, product=product)
        preference.save()
        response = self.client.post('/products/{0}/preference/{1}/'.format(product.id,preference.value),follow=True)
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)
    
    def test_that_the_product_preference_is_not_equal_1(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99')
        product.save()
        preference = Preference(value='1', user=user, product=product)
        preference.save()
        response = self.client.post('/products/{0}/preference/2/'.format(product.id),follow=True)
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_product_preference_is_not_equal_2(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99')
        product.save()
        preference = Preference(value='2', user=user, product=product)
        preference.save()
        response = self.client.post('/products/{0}/preference/1/'.format(product.id),follow=True)
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_product_preference_view_works_without_a_preference_1(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99', likes=0, dislikes=0)
        product.save()
        preference = Preference()
        self.assertRaises(Preference.DoesNotExist, preference.value, 1)
        response = self.client.post('/products/{0}/preference/1/'.format(product.id),follow=True)  
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_product_preference_view_works_without_a_preference_2(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99', likes=0, dislikes=0)
        product.save()
        preference = Preference()
        self.assertRaises(Preference.DoesNotExist, preference.value, 2)
        response = self.client.post('/products/{0}/preference/2/'.format(product.id),follow=True)  
        products = Product.objects.all()
        page = self.client.get('/products/', {'products': products})
        self.assertEqual(page.status_code, 200)

    def test_that_the_product_preference_view_works_without_a_post_method(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99')
        product.save()
        preference = Preference(value='2', user=user, product=product)
        preference.save()
        page = self.client.get('/products/{0}/preference/{1}/'.format(product.id, preference.value), {'products': product})
        self.assertEqual(page.status_code, 200)
    
    

    