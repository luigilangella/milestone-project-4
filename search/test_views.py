from django.test import TestCase
from products.models import Product
class TestTheSearchView(TestCase):

    def test_the_search_view(self):
        """ This test makes sure the search box returns the correct product and renders the page. """
        product = Product(name='vine', price=12.99)
        product.save()
        product_to_search = Product.objects.get(name__icontains='vine')
        
        response = self.client.get('/search/' + '?q=' + product_to_search.name, follow=True) 
        self.assertEqual(response.status_code, 200)