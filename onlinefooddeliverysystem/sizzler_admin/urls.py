from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminhome, name='adminhome'),
    path('menu', views.menu, name='menu'),
    path('orders', views.orders, name='orders')
    # Other URL patterns...
]
