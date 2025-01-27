from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from . import models 
# Create your views here.
def home(request):
    d ={
        'projectname':'FOOD CART'
    }
    return render(request,'home.html',d)
def save(request): 
    if request.method == 'POST':
        obj= models.items()
        obj.itemname = request.POST['itemname']
        obj.itemprice = request.POST['itemprice']
        obj.save()
        return redirect(menu)
    return HttpResponse('<h1> item not Saved </h1>')
def insert(request):
    return render(request,'insert.html')
def menu(request):
    objs = models.items.objects.all()
    d = {
        'records': objs
    }

    return render(request,'menu.html',d)
def modify(request, id):
    obj = models.items.objects.get(id=id)
    d = {
        'record':obj
    }
    return render(request,'modify.html',d)

def update(request):
    if request.method == 'POST':
        obj = models.items.objects.get(id = request.POST['id'])
        obj.itemname = request.POST['itemname']
        obj.itemprice = request.POST['itemprice']
        obj.save()
    return redirect(menu)
    
def delete(request,id): 
    obj = models.items.objects.get(id=id)
    obj.delete()
    return redirect(menu)
def login(request):
    return render(request,'login.html')
def regiester(request):
    return render(request,'regiester.html')
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(f'Username = {username}')
        # print(f'Password = {password}')
        user = authenticate(request, username=username, password=password)
        return render(request,'home.html')
    return render(request,'login.html')
def sigout(request):
    for item,value in request.COOKIES.items():
        print(f'{item} : {value}')
    logout(request)
    return redirect(home)
def forgotpassword(request):
    return render(request,'forgotpassword.html')