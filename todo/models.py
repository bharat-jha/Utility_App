from django.db import models
from datetime import date
from django.contrib.auth.models import User 
# Create your models here.
"The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. "

WORK_CHOICES = (
    ("P", "Personal"),
    ("O", "Official"),
)

STATUS_CHOICES = (
    ("C", "Completed"),
    ("S", "Start"),
    ("W","WIP")  
)

priority_choices = (
    ("L",'LOW'),
    ('M','MEDIUM'),
    ('H','HIGH')
)

class TodoList(models.Model): 
    Category = models.CharField(max_length=1,choices = WORK_CHOICES,default = 'P')
    Description  = models.CharField(max_length = 250)
    Owner = models.ForeignKey(User,on_delete=models.CASCADE) # linking Owner of task to User Created ...
    Status = models.CharField(max_length=1,choices = STATUS_CHOICES,default = 'P')
    Priority = models.CharField(max_length=1 , choices = priority_choices,default = 'L')
    Start_dt = models.DateField(default=date.today)
    End_dt = models.DateField(default=date.today)  
      
    def __str__(self):   
        return(self.Category)