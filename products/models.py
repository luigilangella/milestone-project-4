from django.db import models
from django.contrib.auth.models import User

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class CatalogCategory(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='categories', null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        if self.parent:
            return u'%s : %s - %s' % (self.catalog.name, self.parent.name, self.name)
        else:
            return u'%s : %s' % (self.catalog.name, self.name)

class Product(models.Model):
    category = models.ForeignKey(CatalogCategory, related_name='products', null=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=300, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    manufacturer = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='images')
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name='details')
    attribute  = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return u'%s : %s - %s' % (self.product, self.attribute, self.value)

class ProductAttribute(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return u'%s' % self.name

class Preference(models.Model):
    user= models.ForeignKey(User)
    product= models.ForeignKey(Product)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    
    def __str__(self):
        return str(self.user) + ':' + str(self.product) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "product", "value")     


    
   
    
        
    