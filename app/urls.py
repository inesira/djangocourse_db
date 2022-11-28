from django.contrib import admin
from django.urls import path
from . import views
from app.views import categories


urlpatterns = [
    path('', views.home.index, name='home'),
    path('categories/', views.categories.index, name='categories'),
    path('categories/create', views.categories.create, name='cat_create'),
    path('categories/store', views.categories.store, name='cat_store'),
    path('categories/edit/<int:id>', views.categories.edit, name='cat_edit'),
    path('categories/delete/<int:id>', views.categories.delete, name='cat_delete'),
    ]