from django.conf.urls import url, include
from .views import all_products, productpreference,shop

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<product_id>\d+)/preference/(?P<userpreference>\d+)/$', productpreference, name='productpreference'),
    url(r'^shop$', shop, name='shop'),
]
