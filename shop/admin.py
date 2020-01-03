from django.contrib import admin
from .models import Product , Category , Manufacturer , SubCategory , SubClassification , Cart, CartItem


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubClassification)
admin.site.register(Manufacturer)
admin.site.register(Cart)
admin.site.register(CartItem)


