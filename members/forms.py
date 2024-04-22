
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


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
