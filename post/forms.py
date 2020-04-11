from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """ A form to provide the user the template fields to submit a new blog post. """
    class Meta:
        model = Post
        fields = ['title','content','author','pub_date','image']