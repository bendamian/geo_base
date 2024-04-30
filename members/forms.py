
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput
# create a new user


class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        required=True,
        help_text="<span class='text-info'>Your new password must be at least 8 characters long and include both letters and numbers.</span>"
    )

    new_password2 = forms.CharField(
        label="",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        required=True,
        help_text="<span class='text-info'>Please enter the same password as above, for verification.</span>"
    )

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']





class UpdateUserForm(UserChangeForm):
    password = None

    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=False)

    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=False)

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

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


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

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

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
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)
