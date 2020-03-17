from django.test import TestCase
from .models import Post, User
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.utils import timezone

class TestPostViews(TestCase):

    def test_blog_home_page(self):
        allposts = Post.objects.all() 
        context = {'allposts': allposts} 
        page = self.client.get('/posts/home/', context)
        self.assertEqual(page.status_code, 200)

    def test_create_post_page_with_an_empty_form(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        form  = PostForm()
        page = self.client.get('/posts/create/', {'form':form})
        self.assertEqual(page.status_code, 200)
        

    def test_create_post_page_with_a_form_submitted(self):
        user = User(username='luigi', password='luigi')
        user.save()
        self.client.force_login(user)
        data = {'title':'title', 'content':'content', 'author':'luigi'}
        response = self.client.post('/posts/create/',data=data,follow=True)
        allposts = Post.objects.all() 
        context = {'allposts': allposts} 
        page = self.client.get('/posts/home/', context)
        self.assertEqual(page.status_code, 200)
        

    def test_blog_detail_page(self):
        user = User(username='luigi', password='luigi')
        user.save()
        post = Post()
        post.title = 'title'
        post.content = 'content'
        post.author = user
        post.save()
        page = self.client.get('/posts/{0}/'.format(post.id))
        self.assertEqual(page.status_code, 200)
