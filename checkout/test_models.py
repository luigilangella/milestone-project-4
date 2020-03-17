from django.test import TestCase
from .models import Order, OrderLineItem, Product
# Create your tests here.
class OrderTests(TestCase):
    """ Here we'll define the tests that we'll run
        against our Order model"""

    def test_str(self):
        new_order = Order(full_name='Luigi Langella',id=1,date='')
        self.assertEqual(new_order.__str__(), "id n." + str(new_order.id) + " / date: " + str(new_order.date) + " / Name: " + str(new_order.full_name))

class OrderLineItemTests(TestCase):
    """ Here we'll define the tests that we'll run
        against our OrderLineItem model"""

    def test_str_line_item(self):
        product = Product(name='salami',price=20)
        new_order_line_item = OrderLineItem(quantity=2, product=product)
        self.assertEqual(new_order_line_item.__str__(), str(new_order_line_item.quantity) + " " + str(new_order_line_item.product.name + ' @ ' + str(new_order_line_item.product.price)))
