from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
    pub_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author= models.ForeignKey(User)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    


    def __str__(self):
        return self.title
    
