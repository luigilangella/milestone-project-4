from django.db import models


class Product(models.Model):
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class DeliCounter(models.Model):
    
    cheese = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cheese', blank=True, null=True)
    cured_meats = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cured_meats', blank=True, null=True)
    fresh_meat = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fresh_meat', blank=True, null=True)
    fruit_veg = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fruit_veg', blank=True, null=True)

    def __str__(self):
        return " %s " % (self.cheese or self.cured_meats or self.fresh_meat or self.fruit_veg)

class DryStore(models.Model):
    
    pasta = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pasta', blank=True, null=True)
    oil = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='oil', blank=True, null=True)
    flour = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='flour', blank=True, null=True)
    herbs = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='herbs', blank=True, null=True)

    def __str__(self):
        return " %s " % (self.pasta or self.oil or self.flour or self.herbs)

class Wine(models.Model):
    
    red = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='red', blank=True, null=True)
    white = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='white', blank=True, null=True)
    sparkling = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sparkling', blank=True, null=True)
    spirits = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='spirits', blank=True, null=True)

    def __str__(self):
        return " %s " % (self.red or self.white or self.sparkling or self.spirits)

class Frozen(models.Model):
    
    fish = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fish', blank=True, null=True)
    vegetables = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vegetables', blank=True, null=True)
    meats = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='meats', blank=True, null=True)
    ready_meals = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ready_meals', blank=True, null=True)

    def __str__(self):
        return " %s " % (self.fish or self.vegetables or self.meats or self.ready_meals)

    
   
    
        
    