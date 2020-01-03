from django.shortcuts import render , HttpResponse , redirect
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product, Category , Manufacturer , Cart , CartItem
from .serializers import UserSerializer , ProductSerializer , CategorySerializer , ManufacturerSerializer 
from django import db
db.connections.close_all()

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer

class ProductViewSet(viewsets.ModelViewSet):        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


def detail(request , id):
    product = Product.objects.filter(id=id).first()
    return render(request,"detail.html",{"product":product})

def customerorder(request):
    return render(request,"customer-orders.html")

def customerorders(request):
    return render(request,"customer-orders.html")

def basket(request):
    try:
        the_id = request.session['cart_id']
        #cart = Cart.objects.all()[0]
    except:
        the_id = None
    
    if the_id:
        cart = Cart.objects.get(id=the_id)
        new_total = 0
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            print(new_total)
        
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {"cart" : cart}
    else:
        empty_message = "Your Cart is empty , Please Keep Shopping"
        context = {"empty":True,"empty_message":empty_message}

    print(the_id)
    return render(request,"basket.html" , context)
    

def addToCart(request,id):
    request.session.set_expiry(12000)
    try:
        the_id = request.session['cart_id']
        
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id']= new_cart.id
        the_id=new_cart.id

    cart = Cart.objects.get(id=the_id)
    
    try:
        product = Product.objects.get(id=id)
    
    except Product.DoesNotExist:
        pass
    
    cart_item , created = CartItem.objects.get_or_create(cart = cart ,product=product)

    if created :
        print("Yeah")
    """
    if not cart_item in cart.products.all():
        cart.products.add(product)
        messages.success(request,"Ürün Başarıyla Sepetinize Eklendi ! ")     
    else:
        messages.success(request,"Bu Ürün Zaten Sepetinizde Var ")
    """
    
    messages.success(request,"Ürün Başarıyla Sepetinize Eklendi ! ") 
    return redirect("basket")

def remove_from_cart(request,id):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return redirect("basket")
    
    cartitem = CartItem.objects.get(id=id)
    cartitem.cart = None
    cartitem.save()

    #cartitem.delete()
    #request.session['items_total'] = cart.cartitem_set.count()
    messages.success(request,"Ürün Başarıyla Kaldırıldı ! ") 
    return redirect("basket")
def blog(request):
    return render(request,"blog.html")

def category(request , id):
    if id == 1 :
        products = Product.objects.filter( category_id =1 , subcategory_id = 1 ,subclassification_id = 1 )
        return render(request,"category.html",{"products":products})
    elif id == 2:
        products = Product.objects.filter( category_id =1 , subcategory_id = 1 ,subclassification_id = 2 )
        return render(request,"category.html",{"products":products})
    elif id == 3:
        products = Product.objects.filter( category_id =1 , subcategory_id = 1 ,subclassification_id = 3 )
        return render(request,"category.html",{"products":products})
    elif id == 4:
        products = Product.objects.filter( category_id =1 , subcategory_id = 2 ,subclassification_id = 1 )
        return render(request,"category.html",{"products":products})
    elif id == 5:
        products = Product.objects.filter( category_id =1 , subcategory_id = 2 ,subclassification_id = 2 )
        return render(request,"category.html",{"products":products})
    elif id == 6:
        products = Product.objects.filter( category_id =1 , subcategory_id = 2 ,subclassification_id = 3 )
        return render(request,"category.html",{"products":products})
    elif id == 7:
        products = Product.objects.filter( category_id =1 , subcategory_id = 3 ,subclassification_id = 1 )
        return render(request,"category.html",{"products":products})
    elif id == 8:
        products = Product.objects.filter( category_id =1 , subcategory_id = 3 ,subclassification_id = 2 )
        return render(request,"category.html",{"products":products})
    elif id == 9:
        products = Product.objects.filter( category_id =1 , subcategory_id = 3 ,subclassification_id = 3 )
        return render(request,"category.html",{"products":products})
        
def categoryFull(request):
    product = Product.objects.all()
    return render(request,"category-full.html",{"products":product})

def categoryRight(request):
    return render(request,"category-right.html")

def checkout1(request):
    return render(request,"checkout1.html")

def checkout2(request):
    return render(request,"checkout2.html")

def checkout3(request):
    return render(request,"checkout3.html")

def checkout4(request):
    return render(request,"checkout4.html")

def customerWishlist(request):
    return render(request,"customer-wishlist.html")

def faq(request):
    return render(request,"faq.html")

def post(request):
    return render(request,"post.html")

def textRight(request):
    return render(request,"text-right.html")

def text(request):
    return render(request,"text.html")



def error(request):
    return render(request,"error.html")