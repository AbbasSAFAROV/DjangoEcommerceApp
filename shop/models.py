from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    publication_status = models.BooleanField()

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    publication_status = models.BooleanField()	

    def __str__(self):
        return self.name

class SubClassification(models.Model):
    name = models.CharField(max_length=100)
    publication_status = models.BooleanField()
    	
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    publication_status = models.BooleanField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField()
    image = models.FileField(blank=True, null=True)
    price = models.SmallIntegerField()
    
    stock_lebel = models.SmallIntegerField()
    category_id = models.ForeignKey(Category,on_delete=True)
    subcategory_id = models.ForeignKey(SubCategory,on_delete=True)
    subclassification_id = models.ForeignKey(SubClassification,on_delete=True)
    manufacturer_id = models.ForeignKey(Manufacturer,on_delete=True)
    publication_status = models.BooleanField()
   
    def __str__(self):
        return self.name



class Cart(models.Model):
    total = models.DecimalField(max_digits=100 , decimal_places = 2 , default = 0.00)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id:%s" %(self.id)


    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart , blank=True, null=True , on_delete=True)
    product = models.ForeignKey(Product , on_delete=True)
    line_total = models.DecimalField(max_digits=1000 , decimal_places = 2 , default = 0.00)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        try:
            return str(self.cart.id)
        except :
            return self.product.name



