from django.test import TestCase
from django.core.validators import ValidationError 
from .forms import UserRegistrationForm, User


class TestUserRegistrationForm(TestCase):
    """With this class we perform some tests against
       the user registration form."""
    
    def test_user_registration_form_is_valid(self):
        test_form = UserRegistrationForm({
            'username':'luigi',
            'email':'luigi76langella@gmail.com',
            'password1':'123456',
            'password2':'123456'
        })
        self.assertTrue(test_form.is_valid())
    
    def test_user_registration_form_is_not_valid(self):
        test_form = UserRegistrationForm({
            'username':'luigi',
            'email':'luigi76langella@gmail.com',
            'password1':'1234569',
            'password2':'123456'
        })
        self.assertFalse(test_form.is_valid())
