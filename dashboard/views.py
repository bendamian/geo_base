from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
#from backend.models import Category, Sight, Area
from members.models import Profile
from django.conf import settings
from woodland.models import Woodland

# Create your views here.

#members is in config namespace
#login in members app name
@login_required(login_url='members:login')
def dashboard(request):
    try:
        #profiles = Profile.objects.all()
        print(f"Logged in user: {request.user.username}")  # Debug print
        profiles = get_object_or_404(Profile, user__username=request.user.username)
        print(f"Profile found: {profiles}")  # Debug print
        insects_no = Woodland.objects.filter(category='Insects').count()
        insects_no = int(insects_no)
        print('Number of Insects', insects_no)

        plants_no = Woodland.objects.filter(category='Plants').count()
        plants_no = int(plants_no)
        print('Number of Plants', plants_no)

        birds_no = Woodland.objects.filter(category='Birds').count()
        birds_no = int(birds_no)
        print('Number of Birs', birds_no)

        animal_no = Woodland.objects.filter(category='Animal').count()
        animal_no = int(animal_no)
        print('Number of Animals', animal_no)

        catergory_list = ['Insects', 'Plants', 'Birds', 'Animal']
        catergory_number = [insects_no, plants_no, birds_no, animal_no]
        print('Number of category list', catergory_list)
        print('Number of category number', catergory_number)
    except Profile.DoesNotExist: 
        return redirect('members:login')
    





    context = {
        'profiles': profiles,
        'catergory_list':catergory_list,
        'catergory_number':catergory_number
       

    }
    return render(request, './registration/dashboard.html',context)

