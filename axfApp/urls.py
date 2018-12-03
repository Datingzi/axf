from django.conf.urls import url
from axfApp import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^home/$', views.home, name="home"),
    url(r'^market/(\w+)/$', views.market, name="market"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^mine/$', views.mine, name="mine"),
]
