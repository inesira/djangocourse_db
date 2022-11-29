from django.contrib import admin
from django.urls import path
from . import views
from app.views import categories
from app.views import products


urlpatterns = [
    path('', views.home.index, name='home'),
    path('categories/', views.categories.index, name='categories'),
    path('categories/create', views.categories.create, name='cat_create'),
    path('categories/store', views.categories.store, name='cat_store'),
    path('categories/edit/<int:id>', views.categories.edit, name='cat_edit'),
    path('categories/delete/<int:id>', views.categories.delete, name='cat_delete'),

    path('products/', views.products.index, name='products'),
    path('products/create', views.products.create, name='produit_create'),
    path('products/store', views.products.store, name='produit_store'),
    path('products/edit/<int:id>', products.edit, name='produit_edit'),
    path('products/delete/<int:id>', views.products.delete, name='produit_delete'),
    
    
    path('customers/', views.customers.index , name='customer'),
    path('customers/create', views.customers.create, name='cust_create'),
    path('customers/store', views.customers.store, name='cust_store'),
    path('customers/edit/<int:id>', views.customers.edit, name='cust_edit'),
    path('customers/delete/<int:id>', views.customers.delete, name='cust_delete'),
    ]