from django.contrib import admin
from .models import Product, Catalog, CatalogCategory, ProductAttribute, ProductDetail, Preference

# Register your models here.
admin.site.register(Product)
admin.site.register(Preference)
admin.site.register(Catalog)
admin.site.register(CatalogCategory)
admin.site.register(ProductAttribute)
admin.site.register(ProductDetail)