"""food_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home.views import index
from search import urls as urls_search
from products import urls as urls_products
from products.views import shop
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from post import urls as urls_post
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^shop', shop, name='shop'),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/',include(urls_checkout)),
    url(r'^posts/', include(urls_post)),
    url(r'^search/',include(urls_search)),
    url(r'^media(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
