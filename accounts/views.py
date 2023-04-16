from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignUp_form,Profile_Form,AdminProfile_Form,Contact_Form
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# defining the home view - default values........
def home(request): 
    return(render(request,'accounts/profile.html',{'title': 'profile','form':UserChangeForm}))

def aboutus(request):  
    return(render(request,'accounts/About_us.html'))

# user Profile Page for
@login_required
def profile(request): 
    data = User.objects.filter(username=request.user.username)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            fm = AdminProfile_Form(request.POST,instance=request.user)
            users = User.objects.all()
            print(users)
        else:  
            users=None
            fm = Profile_Form(request.POST,instance=request.user)
        if request.method == 'POST':
            if fm.is_valid(): 
                fm.save()
                messages.success(request,"Your Profile has been updated")
                return(redirect("accounts:Login"))
        else: 
            if request.user.is_superuser:
                users = User.objects.all()
                print(users)
                fm = AdminProfile_Form(instance=request.user)
            else:
                users=None
                fm = Profile_Form(instance=request.user)
    else: 
        return(redirect("accounts:Login"))
    return(render(request,'accounts/profile.html',{'title': 'profile','form':fm,'users':users}))

# Registration form for the users ... 
def SignUp(request):
    if request.method == 'POST':
        fm = SignUp_form(request.POST)
        if fm.is_valid():
            print(fm)
            fm.save()
            messages.success(request,"Your Account has been created ")
            return(redirect("accounts:Login"))
    else:
        fm = SignUp_form()
    return(render(request,'accounts/sign_up.html',{'form':fm}))

# User Login form for tha analysis ....
def user_login(request): 
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["username"]
            passwd = fm.cleaned_data['password']
            user = authenticate(username = nm, password = passwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Welcome Back "+str(request.user))
                return(redirect("home"))
    else: 
        fm = AuthenticationForm()
    return(render(request,'accounts/user_login.html',{'form':fm}))

# Logging out the User : Remember Logging out from session will delete all session data and associated cookies ...
def user_logout(request):
    logout(request)
    return(redirect("accounts:Login"))

# Changing the password : when we have old password ................
@login_required
def changePass(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Kindly Login with New Password !!")
                update_session_auth_hash(request,request.user)
                return(redirect("accounts:Login"))
        else:
            fm = PasswordChangeForm(user=request.user)
    else: 
        return(redirect("accounts:Login"))
    return(render(request,'accounts/changepassword.html',{'form' :fm}))

# Defining the user details function for the analysis ................
@login_required
def user_detail(request,id): 
    user = User.objects.get(pk=id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = AdminProfile_Form(request.POST,instance=user)
            if fm.is_valid() : 
                fm.save()  
                messages.success(request,"Profile has been updated!!")
                return(redirect("accounts:profile"))
        else:  
            fm = AdminProfile_Form(instance=user)
    else: 
        return(redirect("accounts:Login"))
    return(render(request,'accounts/user_details.html',{'form':fm}))



def contact(request): 
    if request.method == 'POST':
        fm = Contact_Form(request.POST)
        if fm.is_valid() : 
            fm.save() 
            messages.success(request,"Thanks for contacting us !!  We will get in touch soon ")
            return(redirect("home"))
    else:
        fm = Contact_Form()  
    return(render(request,'accounts/contact_form.html',{'fm': fm}))