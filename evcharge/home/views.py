from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import stationdetails
from .models import reviews
from json import dumps

# Create your views here.

def index(request):
    return render(request, "index.html")

def map(request):
    stationdetail =list(stationdetails.objects.all())
   
    dataset=[]
    # dump data
   
    for i in range(0,len(stationdetail)):
        print(stationdetail[i].name)
        dataDictionary = {
        'name': stationdetail[i].name,
        'latitude': stationdetail[i].latitude,
        'longitude': stationdetail[i].longitude,
        'chargeprice': stationdetail[i].chargeprice,
        'charger': stationdetail[i].charger
        }
        dataJSON = dumps(dataDictionary)
        dataset.append(dataDictionary)
    return render(request,'map.html',{'data': dumps(dataset)})

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
        stationdetail =list(stationdetails.objects.all())
        dataset=[]
        # dump data
    
        for i in range(0,len(stationdetail)):
            print(stationdetail[i].name)
            dataDictionary = {
            'name': stationdetail[i].name,
            'latitude': stationdetail[i].latitude,
            'longitude': stationdetail[i].longitude,
            'chargeprice': stationdetail[i].chargeprice,
            'charger': stationdetail[i].charger
            }
            dataJSON = dumps(dataDictionary)
            dataset.append(dataDictionary)
        return render(request,'addpoint.html',{'data': dumps(dataset)})
    else:
        return render(request, 'login.html')
    
def details(request):
    return render(request,'details.html')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        price = request.POST.get('price')
        chargetype = request.POST.get('chargetype')
        address = request.POST.get('address')
        print(chargetype)
        print(latitude)

        en = stationdetails(name=name,latitude=latitude,longitude=longitude,chargeprice=price,charger=chargetype,address=address)
        en.save()
        print('helo')
    else:
        pass
    return render(request, 'addpoint.html')

def details(request, name):
    stationdetail =list(stationdetails.objects.filter(name=name).all())
    reviewset =list(reviews.objects.filter(stationname=name).all())
    # stationdetail =list(stationdetails.objects.all())
    dataset=[]
        # dump data
    for i in range(0,len(reviewset)):
        dataDictionary = {
        'username': reviewset[i].username,
        'highlights': reviewset[i].highlights,
        'rating': reviewset[i].rating,
        'description': reviewset[i].description
        }
        dataJSON = dumps(dataDictionary)
        dataset.append(dataDictionary)
        datasetmain = {
            "data": dataDictionary
        }
   
    return render(request,'details.html',{'data': dumps(dataset),'stationname':name, 'price':stationdetail[0].chargeprice, 'address':stationdetail[0].address, 'charger':stationdetail[0].charger })
    # return render(request, 'details.html')

def addreviews(request, stationname):
    print(stationname)
    print('-------------------')
    print(request.POST.get('highlights'))
    if request.method == 'POST':
        username = request.POST.get('username')
        highlights = request.POST.get('highlights')
        rating = request.POST.get('myRange')
        description = request.POST.get('description')

        en = reviews(username=username,stationname=stationname,highlights=highlights,rating=rating,description=description)
        en.save()
    else:
        pass
    return render(request, 'map.html')