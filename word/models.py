from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100)
    
    
class Vocab(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000,default="None")
    search_dt = models.DateField(default=timezone.now)