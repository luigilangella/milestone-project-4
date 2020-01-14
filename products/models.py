from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    
    name = models.CharField(max_length=254, default='', unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Preference(models.Model):
    user= models.ForeignKey(User)
    product= models.ForeignKey(Product)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    
    def __str__(self):
        return str(self.user) + ':' + str(self.product) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "product", "value")     

class DeliCounter(models.Model):
    
    cheese = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cheese', blank=True, null=True, to_field='name')
    cured_meats = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cured_meats', blank=True, null=True, to_field='name')
    fresh_meat = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fresh_meat', blank=True, null=True, to_field='name')
    fruit_veg = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fruit_veg', blank=True, null=True, to_field='name')

    def __str__(self):
        return " %s " % (self.cheese or self.cured_meats or self.fresh_meat or self.fruit_veg)

class DryStore(models.Model):
    
    pasta = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pasta', blank=True, null=True, to_field='name')
    oil = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='oil', blank=True, null=True, to_field='name')
    flour = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='flour', blank=True, null=True, to_field='name')
    herbs = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='herbs', blank=True, null=True, to_field='name')

    def __str__(self):
        return " %s " % (self.pasta or self.oil or self.flour or self.herbs)

class Wine(models.Model):
    
    red = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='red', blank=True, null=True, to_field='name')
    white = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='white', blank=True, null=True, to_field='name')
    sparkling = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sparkling', blank=True, null=True, to_field='name')
    spirits = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='spirits', blank=True, null=True, to_field='name')

    def __str__(self):
        return " %s " % (self.red or self.white or self.sparkling or self.spirits)

class Frozen(models.Model):
    
    fish = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fish', blank=True, null=True, to_field='name')
    vegetables = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vegetables', blank=True, null=True, to_field='name')
    meats = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='meats', blank=True, null=True, to_field='name')
    ready_meals = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ready_meals', blank=True, null=True, to_field='name')

    def __str__(self):
        return " %s " % (self.fish or self.vegetables or self.meats or self.ready_meals)

    
   
    
        
    