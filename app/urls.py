from django.contrib import admin
from django.urls import path
from . import views
from app.views import categories


urlpatterns = [
    path('', views.home.index, name='home'),
    path('categories/', views.categories.index, name='categories'),
    ]