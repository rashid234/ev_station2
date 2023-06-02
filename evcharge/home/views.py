from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def map(request):
    return render(request,'map.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            if User.objects.filter(username='admin'):
                return redirect('addpoint')
            else:
                return redirect('index.html')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    else:
        if request.user.is_authenticated:
            if User.objects.filter(username='admin'):
                return redirect('addpoint')
            else:
                return redirect('index.html')
        else:
            return render(request,"login.html")

def register(request):
    return render(request, "index.html")

def logout(request):
    auth_logout(request)
    return redirect('./')
    

def addpoint(request):
    if User.objects.filter(username='admin'):
        return render(request, 'addpoint.html')
    else:
        return render(request, 'login.html')
    
def details(request):
    return render(request,'details.html')