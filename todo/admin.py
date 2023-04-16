from django.contrib import admin
from .models import  TodoList

# Register your models here.
@admin.register(TodoList) 
class Admin(admin.ModelAdmin):
    list_display = ['Category','Description','Owner','Status','Start_dt','End_dt']
    search_fields = ('Category','Description','Owner','Status','Start_dt','End_dt')
    
