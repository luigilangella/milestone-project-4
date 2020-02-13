from django.conf.urls import url
from django.contrib import admin
from .views import (createpost, detail_post_view, home)

urlpatterns = [
     url(r'^home/$', home, name='home'),
     url(r'^create/', createpost, name='createpost'),
     url(r'^(?P<id>\d+)/$', detail_post_view, name='detail'),
     ]