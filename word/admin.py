from django.contrib import admin
from .models import Word,Vocab


# Register your models here.
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_fields = ['word']
    
@admin.register(Vocab)
class WordAdmin(admin.ModelAdmin):
    list_fields = ['User','word','search_dt']