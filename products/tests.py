from django.test import TestCase
from .models import Product, DeliCounter

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

    def test_price(self):
        test_price = Product(price=12.55)
        self.assertEqual(test_price.price, 12.55)

class DeliCounterTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    DeliCounter model
    """

    def test_cheese_section_add(self):
        test_name = DeliCounter(cheese=Product(name='salami'))
        self.assertIn('salami',str(test_name))
    def test_cured_meats_section_add(self):
        test_name = DeliCounter(cured_meats=Product(name='prosciutto'))
        self.assertIn('prosciutto',str(test_name))