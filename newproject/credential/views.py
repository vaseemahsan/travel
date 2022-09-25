from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credential')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['First name']
        lastname=request.POST['Last Name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)

            user.save();
            print('user created')
            return redirect('login')

        else:
            messages.info(request,'password does not match')
            return redirect('register')
        return redirect('/')


    return render(request,'register.html')