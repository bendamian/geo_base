
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput,TextInput
#create a new user 
class CreateUserForm(UserCreationForm):


    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Authenticate a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-1 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-1 px-6 rounded-xl'
    }))
