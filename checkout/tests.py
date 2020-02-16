from django.test import TestCase
from .models import Order, OrderLineItem, Product
# Create your tests here.
class OrderTests(TestCase):
    """ Here we'll define the tests that we'll run
        against our Order model"""

    def test_str(self):
        new_order = Order(full_name='Luigi Langella',id=1,date='')
        self.assertEqual(new_order.full_name, 'Luigi Langella')
        self.assertEqual(new_order.id, 1)
        self.assertEqual(new_order.date, '')

class OrderLineItemTests(TestCase):
    """ Here we'll define the tests that we'll run
        against our OrderLineItem model"""

    def test_str_line_item(self):
        product = Product(name='salami',price=20)
        new_order_line_item = OrderLineItem(quantity=2, product=product)
        self.assertEqual(new_order_line_item.quantity, 2)
        self.assertEqual(new_order_line_item.product.name, 'salami')
        self.assertEqual(new_order_line_item.product.price, 20)