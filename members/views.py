from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import LoginForm, SignupForm ,UpdateUserForm,ChangePasswordForm
# Create your views here.


def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('/members/dashbord')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('/members/update_password/')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "./registration/update_password.html", {'form': form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('/')







def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		form = UpdateUserForm(request.POST or None, instance=current_user)

		if form.is_valid():
			form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('/')
		return render(request, "./registration/update_user.html", {'form': form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('/')



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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/members/login_user/')
    else:
        form = SignupForm()

    return render(request, './registration/register.html', {
        'form': form
    })


def logout_user(request):
    logout(request)
    #auth.logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect("/")
