from django.test import TestCase
from .models import Post, User

class TestPostModel(TestCase):

    def test_str_post_model(self):
        user_logged_in = User(username='luigi')
        new_post = Post(title='test', author=user_logged_in)
        self.assertEqual(
            new_post.__str__(), (str(new_post.title) + ' ' + str(new_post.author))
        )