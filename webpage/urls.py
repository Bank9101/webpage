from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product-info/', views.product_info, name='product_info'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('topup/', views.topup, name='topup'),
    path('sales/', views.sales, name='sales'),
] 