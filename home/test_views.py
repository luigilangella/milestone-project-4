from django.test import TestCase
from products.models import Product

class TestHomeView(TestCase):

    def test_home_view(self):
        """ This test makes sure the home page is rendered correctly. """
        product = Product(name='vine', price=12.99)
        product.save()
        products = Product.objects.all()
        page = self.client.get('/', {'products':products})
        self.assertEquals(page.status_code, 200)
