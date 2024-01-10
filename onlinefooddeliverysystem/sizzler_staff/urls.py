from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.staff_login, name='staff_login'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('process_order/<int:pk>/', views.process_order, name='process_order'),
]