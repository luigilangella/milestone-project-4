from django.contrib import admin
from .models import Product, DeliCounter, DryStore, Frozen, Wine

# Register your models here.
admin.site.register(Product)
admin.site.register(DeliCounter)
admin.site.register(DryStore)
admin.site.register(Frozen)
admin.site.register(Wine)