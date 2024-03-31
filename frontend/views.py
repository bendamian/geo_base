from django.shortcuts import render
from backend.models import Category,Sight
from django.urls import path

# Create your views here.
def home_view(request,*args,**kwargs):
    context={}
    return render(request,'./frontend/pages/index.html',context) 

def world_view(request,*args,**kwargs):
    context={}
    return render(request,'./frontend/pages/world.html',context) 