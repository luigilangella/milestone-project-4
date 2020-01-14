from django.contrib import admin
from .models import Product, DeliCounter, DryStore, Frozen, Wine, Preference

# Register your models here.
admin.site.register(Product)
admin.site.register(Preference)
admin.site.register(DeliCounter)
admin.site.register(DryStore)
admin.site.register(Frozen)
admin.site.register(Wine)