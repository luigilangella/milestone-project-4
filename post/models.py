from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Post(models.Model):
    """ This Post models allows the logged in user to create a new post and upload an image. """
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
    pub_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author= models.ForeignKey(User)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    


    def __str__(self):
        return '%s %s' %(self.title, self.author)
    
