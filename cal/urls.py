from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'cal'
urlpatterns = [
    path('index/', views.index,name='home') ,
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:id>/', views.event_edit, name='event_edit'),
    path('event/delete/<int:id>/', views.event_delete, name='event_delete'),
]