from django.shortcuts import render , redirect
from django.views import View
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.hashers import check_password


# Create your views here.

def home(request):
    return render(request,'index.html')

class Signup(View):
    def get(self,request):
        return render(request,'sign-up.html')
    def post(self,request):
        d = request.POST
        if not (d.get('fname') and d.get("lname") and d.get("phonenumber") and d.get("email") and d.get("password") and d.get("password")):
            message = "All Fields are required"
            return render(request,"sign-up.html", {"message" : message})

        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get("password")
        password2 = request.POST.get("password")
        if password==password2:
            data = User()
            data.first_name = firstname
            data.last_name = lastname
            data.email = email
            data.set_password(password)
            data.mobile = phonenumber

            data.save()
            
            return redirect('login')
        else:
            messages.error(request, "Password does not match")
            return redirect("signup")


def user_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method =="POST":	
        d = request.POST
       
        email = request.POST.get('email')
        
        password = request.POST.get('password')
        us = User.objects.get(email=email)
        print(us.first_name)
        # for u in us:
            # print(u.email)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html')


def dashboard(request):
    # Name = request.user
    return render(request, 'dashboard.html')

def TopUp(request):
    return render(request, 'topup.html')

def User_Logout(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("home")

def WithDraw(request):
    return render(request, 'withdrow.html')

def Send(request):
    return render(request,"send.html")

def Invoicing(request):
    return render(request,"invoicing.html")

def Utilities(request):
    return render(request,"utilities.html")

def Reports(request):
    return render(request,"reports.html")

def User_Profile(request):
    return render(request, "userprofile.html")