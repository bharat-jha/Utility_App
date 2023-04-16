from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Subject(models.Model): 
    subject = models.CharField(max_length=50,unique=True,default="Others") 
    def __str__(self): 
        return(str(self.subject))


class Note(models.Model): 
    Topic = models.ForeignKey(Subject, related_name='topic',on_delete=models.CASCADE)
    Description = models.TextField()
    pic = models.ImageField(upload_to="images/" )
    date_create = models.DateField(auto_now_add=True, blank=True)
    date_update = models.DateField()
    status = models.CharField(max_length = 1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE) #
    
    def __str__(self):   
        return(self.Topic)
    
    