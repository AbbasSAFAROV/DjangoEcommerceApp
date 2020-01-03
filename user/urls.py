from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Userlogin , name = "login"),
    path('signin/', views.signin , name = "signin"),
    path('logout/', views.Userlogout , name = "logout"),
    path('register/', views.register , name = "register"),
    path('customer-account/', views.userAccount , name = "userAccount"),
    
]
