from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User 
from django import forms 
from .models import Contact
from django.forms import ModelForm

class SignUp_form(UserCreationForm): 
    password2 = forms.CharField(label="Password(Again)",widget=forms.PasswordInput())
    class Meta: 
        model =User 
        fields= ['username','email','first_name','last_name']

class Profile_Form(UserChangeForm):
    password = None #
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','last_login']
        labels ={'email':"Email Address"}

class AdminProfile_Form(UserChangeForm):
    password = None
    class Meta:
        model = User
        exclude  = ['password']
        labels ={'email':"Email Address"}


class Contact_Form(ModelForm):
    class Meta:
        model = Contact
        exclude  = ['password']
        labels ={'email':"Email Address"}