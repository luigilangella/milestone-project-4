from django.conf.urls import url, include
from .views import all_products, productpreference,shop, wines

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<product_id>\d+)/preference/(?P<userpreference>\d+)/$', productpreference, name='productpreference'),
    url(r'^shop$', shop, name='shop'),
    url(r'^wines/', wines, name='wines'),
]
