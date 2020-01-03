from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path('customer-order/', views.customerorder, name = "customer-order"),
    path('customer-orders/', views.customerorders, name = "customer-orders"),
    path('detail/<int:id>', views.detail, name = "detail"),
    path('basket/', views.basket, name = "basket"),
    path('basket/<int:id>', views.addToCart, name = "addToCart"),
    path('blog/', views.blog, name = "blog"),
    path('category/<int:id>', views.category, name = "category"),
    path('delete/<int:id>', views.remove_from_cart, name = "remove_from_cart"),
    path('category-full/', views.categoryFull, name = "categoryFull"),
    path('category-right/', views.categoryRight, name = "categoryRight"),
    path('checkout1/', views.checkout1, name = "checkout1"),
    path('checkout2/', views.checkout2, name = "checkout2"),
    path('checkout3/', views.checkout3, name = "checkout3"),
    path('checkout4/', views.checkout4, name = "checkout4"),
    path('custormerwishlist/', views.customerWishlist, name = "customerWishlist"),
    path('faq/', views.faq, name = "faq"),
    path('post/', views.post, name = "post"),
    path('text/', views.text, name = "text"),
    path('text-right/', views.textRight, name = "textRight"),
    path('error/', views.error, name = "error"),


]
