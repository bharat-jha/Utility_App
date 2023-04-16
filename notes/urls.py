from django.contrib import admin
from django.urls import path,include
from . import views


# Define url patterns here ...
app_name  = 'notes'
urlpatterns = [
   path('subject/',views.subject,name='subject_entry'),
   path('notes_form/',views.notes_entry,name='notes_entry'),
   path('notes_list/',views.notes_list,name='notes_list'),
   path('update/<int:id>/',views.notes_update,name='update'),
   path('delete/<int:id>/',views.notes_delete,name='delete'),
]