from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('product_api',views.ProductViewSet)
router.register('category_api',views.CategoryViewSet)
router.register('manufacturer_api',views.ManufacturerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
