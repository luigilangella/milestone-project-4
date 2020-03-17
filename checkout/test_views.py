from django.test import TestCase
from products.models import User, Product
from .forms import MakePaymentForm, OrderForm
from django.conf import settings



class TestCheckOutView(TestCase):

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
        

    # def test_the_checkout_order_form_and_payment_form_is_valid(self):
    #     user = User(username='luigi', password='luigi', email='luigi76langella@gmail.com')
    #     user.save()
    #     self.client.force_login(user)
    #     product = Product(name='Vino Rosso Chianti', price='12.99', pk=1)
    #     product.save()
    #     order_form_data = {
    #         'full_name':'Luigi Langella',
    #         'phone_number': '07496656778',
    #         'country': 'UK',
    #         'postcode':'TQ14PG',
    #         'town_or_city':'Torquay',
    #         'street_address1':'17, Shelley Avenue',
    #         'street_address2':'Torquay',
    #         'county':'Devon'
    #     }
    #     payment_form_data = {
    #         'credit_card_number':'',
    #         'cvv':'',
    #         'expiry_month':'',
    #         'expiry_date':'',
    #         'stripe_id': settings.STRIPE_SECRET
    #     }
    #     payment_form = MakePaymentForm(data=payment_form_data)
    #     order_form = OrderForm(data=order_form_data)
    #     order_form.date = timezone.now()
    #     order_form.save(commit=False)
    #     self.assertTrue(order_form.is_valid())
    #     self.assertTrue(payment_form.is_valid())
    #     response = self.client.post('/checkout/', {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE},follow=True)
    #     self.assertEqual(response.status_code, 200)

    


