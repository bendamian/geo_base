from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CreateUserForm, LoginForm
# Create your views here.


def login_user(request):

    form = LoginForm()


    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashbord')
            else:
                messages.success(request, ("There Was An Error Logging In, Try Again..."))
                return redirect('login')

    
    
   
    context = {'form': form}
    return render(request, './registration/login.html', context=context)


def dashbord(request):

    context = {}
    return render(request, './registration/dashbord.html',context) 