from django.contrib import admin
from .models import Note,Subject
# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):  
    list_display = ['Topic','Description','date_create','date_update','status','owner']  
    search_fields = ['Topic','Description','date_create','date_update','status','owner']
    
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):  
    list_display = ['subject']  
    search_fields = ['subject']