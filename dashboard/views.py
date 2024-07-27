from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
#from backend.models import Category, Sight, Area
from members.models import Profile
from django.conf import settings

# Create your views here.


@login_required(login_url='/members/login_user/')
def dashboard(request):
    try:
        #profiles = Profile.objects.all()
        print(f"Logged in user: {request.user.username}")  # Debug print
        profiles = get_object_or_404(Profile, user__username=request.user.username)
        print(f"Profile found: {profiles}")  # Debug print
    except Profile.DoesNotExist: 
        return redirect('/members/login_user/')
    
    context = {
        'profiles': profiles,
       

    }
    return render(request, './registration/dashboard.html',context)
