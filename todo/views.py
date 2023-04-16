from django.shortcuts import render,redirect
from .models import TodoList
from .forms import Addtask
from django.contrib import messages # message session
from .models import TodoList
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here...
@login_required
def addTodo(request): 
    current_user = request.user.id 
    todo = TodoList.objects.all().filter(Owner_id=current_user)
    if request.method=="POST": 
        fm= Addtask(request.POST)
        if fm.is_valid(): 
            category = fm.cleaned_data["Category"]
            description = fm.cleaned_data["Description"]
            status = fm.cleaned_data["Status"]
            priority = fm.cleaned_data["Priority"]
            start_dt = fm.cleaned_data["Start_dt"]
            end_dt = fm.cleaned_data["End_dt"]
            task = TodoList(Category=category, Description=description, Status=status,Owner = request.user, Priority=priority,Start_dt=start_dt,
                            End_dt= end_dt)
            task.save()
            fm = Addtask()
            messages.success(request," New tasks has been Created !!!")
    else: 
        fm = Addtask()  
    return(render(request,"todo/home.html",{'title' :"Home Page","todo":todo,'fm':fm}))
@login_required
def todo_delete(request,id):
    todo_item = TodoList.objects.get(pk=id) 
    todo_item.delete()
    messages.success(request,"Tasks has been deleted !!")
    return(redirect("home"))
@login_required
def todo_update(request,id):  
    todo_item = TodoList.objects.get(pk=id) 
    if request.method == "POST":
        fm = Addtask(request.POST,instance=todo_item)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Tasks has been Updated !!!") # shortcut way of passing info...
            return(redirect("home"))
    else: 
        fm = Addtask(instance=todo_item)
    return(render(request,'todo/todo_update.html',{"fm":fm}))