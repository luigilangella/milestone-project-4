from django.test import TestCase
from products.models import User, Product
from .forms import MakePaymentForm, OrderForm
from django.conf import settings



class TestCheckOutView(TestCase):
    """ A test to make sure the check out view works as expected. """
    def test_the_checkout_page_view(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        product = Product(name='Vino Rosso Chianti', price='12.99')
        product.save()
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        response = self.client.post('/checkout/', {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE},follow=True)
        self.assertEqual(response.status_code, 200)


    


