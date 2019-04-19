from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import *


def register(request):
    if request.method =="POST":
        forms = UsersiginupForms(request.POST)
        if forms.is_valid():

            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]
            confirm_password = forms.cleaned_data["confirm_password"]
            email = forms.cleaned_data["email"]

            if password!=confirm_password:
                errMsg = "Password and Confirm Password Not same"
                context = {"errMsg":errMsg,
                            "form":forms
                            }
                return render(request,'author/register.html',context)

            if not User.objects.filter(username=username).exists():

                User.objects.create_user(username,email,password)
                return redirect("login")
            
    forms = UsersiginupForms()
    context={"form":forms}
    return render(request,'author/register.html',context)



def userlogin(request):
    if request.user.is_authenticated:
       return redirect('home')

    else:
        if request.method=="POST":
            form = userloginform(request.POST)
            if form.is_valid():
                username= form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = authenticate(username=username, password=password)
    
                if user:
                    login(request,user)
                    return redirect("home")
                else:
                    errMsg = "User name or password invalid"
                    context = {
                        "errMsg":errMsg,
                        "froms":form
                        }
                    return render(request,"author/login.html",context)
                    
    form = userloginform()
    context = {
        "forms":form
        }
    return render(request,"author/login.html",context)

def userlogout(request):
    logout(request)
    return redirect("home")