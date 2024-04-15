from django.shortcuts import render,redirect
from backend.models import Category,Sight,Area
from .forms import AreaForm
from django.urls import path

# Create your views here.
def home_view(request,*args,**kwargs):
    context={}
    return render(request,'./frontend/pages/index.html',context) 

def world_view(request,*args,**kwargs):
    context={}
    return render(request,'./frontend/pages/world.html',context) 


def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/world')
    else:
        form = AreaForm()
    return render(request, './frontend/pages/add_area.html', {'form': form})





