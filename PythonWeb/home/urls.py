from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name = 'contact'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView, {'template': 'pages/login.html'}, name = 'login')
]