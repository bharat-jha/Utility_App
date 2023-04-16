from django.urls import path
from . import views
from django.urls import reverse_lazy


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp, name="signup"),
    path('login/', views.user_login, name="Login"),  
    path('logout/', views.user_logout, name="Logout"), 
    path('password_change/',views.changePass,name='password_change'),
    path('profile/',views.profile,name='profile'), 
    path('user_profile/<int:id>/', views.user_detail,name='user_detail'),
    path('contact/', views.contact, name="contact"),
    path('Aboutus/',views.aboutus, name="Aboutus"),
]