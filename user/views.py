from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages


def Userlogin(request):

    if request.method == "POST":
        loginemail = request.POST.get("loginemail")
        loginpassword = request.POST.get("loginpassword")

        user = authenticate(email = loginemail , password = loginpassword)

        if user is None:
            messages.info(request,"kullanici veya parola hatali")

        messages.success(request,"başarıyla giriş yaptınız")
        login(request,user)
        return redirect("index")

    return render(request,"index.html")

def signin(request):

    if request.method == "POST":
        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")

        user = authenticate(username = loginusername , password = loginpassword)

        if user is None:
            messages.warning(request,"kullanici veya parola hatali")

        else:
            messages.success(request,"başarıyla giriş yaptınız")
            login(request,user)
            return redirect("index")

    return render(request,"signin.html")

def Userlogout(request):
    logout(request)
    messages.success(request,"başarıyla çıkış yaptınız...")
    return redirect("index")

def register(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        userpassword = request.POST.get("userpassword")

        newUser = User(username = username , email = useremail)
        newUser.set_password(userpassword)

        newUser.save()
        login(request, newUser)
        messages.success(request,"başarıyla kayıt oldunuz . . .")
        return redirect("index")

    else:
        return render(request,"register.html")

def userAccount(request):
    return render(request,"customer-account.html")
