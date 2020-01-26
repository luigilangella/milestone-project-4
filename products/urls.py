from django.conf.urls import url, include
from .views import all_products, productpreference,shop, wines, dairy, cured_meats, fruit_and_veg, fish_fresh, fish_frozen, dry_store

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<product_id>\d+)/preference/(?P<userpreference>\d+)/$', productpreference, name='productpreference'),
    url(r'^shop$', shop, name='shop'),
    url(r'^wines/', wines, name='wines'),
    url(r'^dairy/', dairy, name='dairy'),
    url(r'^cured_meats/', cured_meats, name='cured_meats'),
    url(r'^fruit_and_veg/', fruit_and_veg, name='fruit_and_veg'),
    url(r'^fish_fresh/', fish_fresh, name='fish_fresh'),
    url(r'^fish_frozen/', fish_frozen, name='fish_frozen'),
    url(r'^dry_store/', dry_store, name='dry_store'),
]
