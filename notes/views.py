from django.shortcuts import render,redirect
from .models import Note,Subject
from .forms import  Notes_Form,Subject_Form
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def subject(request):  
    if request.method == 'POST': 
        sub = Subject_Form(request.POST) 
        if sub.is_valid(): 
            sub.save() 
            redirect('home') 
    else: 
        sub = Subject_Form()
    return(render(request,'notes/subject_form.html',{'sub':sub}))

@login_required
def notes_entry(request):  
    if request.method == 'POST': 
        notes_form = Notes_Form(request.POST, request.FILES)
 
        if notes_form.is_valid(): 
            topic = notes_form.cleaned_data['Topic']
            description = notes_form.cleaned_data['Description']
            date_update = notes_form.cleaned_data['date_update']
            status = notes_form.cleaned_data['status']
            img = notes_form.cleaned_data['pic']
            owner = request.user
            data = Note(Topic=topic,Description=description,date_update=date_update,
                       status = status,owner=owner,pic=img )
            data.save() 
            messages.success(request,"New Note has been updated!!")
            return(redirect('notes:notes_list'))
    else: 
        notes_form  = Notes_Form()
    return(render(request,'notes/notes_form.html',{'notes_form':notes_form }))

# Listing all notes ...
@login_required
def notes_list(request):   
    current_user = request.user.id 
    notes = Note.objects.all().filter(owner_id=current_user)
    return(render(request,"notes/home.html",{'title' :"Home Page","notes":notes}))

@login_required
def notes_update(request,id):   
    note_item = Note.objects.get(pk=id) 
    if request.method == "POST":
        fm = Notes_Form(request.POST,instance=note_item)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Note has been Updated !!!") # shortcut way of passing info...
            return(redirect("notes:notes_list"))
    else: 
        fm = Notes_Form(instance=note_item)
    return(render(request,'notes/notes_update.html',{"fm":fm}))

@login_required
def notes_delete(request,id):   
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request,"Note has been Deleted!!")
    return(redirect("notes:notes_list"))