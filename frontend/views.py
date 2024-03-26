from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    context={}
    return render(request,'./frontend/pages/index.html',context) 