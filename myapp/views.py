from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Custom_User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_signup(request):
    return render(request,'register.html')

def user_login(request):
    return render(request, 'login.html')

def handle_signup(request):
    name = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    dob = request.POST['dob']

    try:
        user = Custom_User.objects.filter(username=username).count()
    except:
        return redirect('login')
    
    if user == 0:
        user = Custom_User.objects.create_user(username=username, email=email, password=password)
        user.DOB = dob
        user.first_name = name

        user.save()
        return redirect('login')

    else :  
        return render(request, 'register.html', {'exist':True})

    
    return redirect('login')

def handle_login(request):
    usern = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=usern, password=password)

    if user is not None:
        login(request, user)
        user = Custom_User.objects.filter(username=usern).get()
        return render(request, 'home.html', {'data':user})
    else:
       
       return render(request, 'login.html',{'invalidCred':True})



