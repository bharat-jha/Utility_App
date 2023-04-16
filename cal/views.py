from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar
from .forms import EventForm
import calendar
from django.contrib import messages
from django.contrib.auth.decorators import login_required

now=datetime.now()
# Create your views here.
def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'
    queryset = Event.objects.filter(start_time__date = date.today())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request,id=None):
    if request.method=="POST": 
        fm = EventForm(request.POST)
        if fm.is_valid(): 
            fm.save()
            messages.success(request," New Event has been Created !!!")
            return(redirect('cal:calendar'))
    else: 
        fm = EventForm() 
    return render(request, 'cal/event.html', {'form': fm,'id':id})
@login_required   
def event_edit(request,id):
    data = Event.objects.get(pk=id)
    if request.method == "POST":
        form = EventForm(request.POST , instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Event added !")
            return HttpResponseRedirect(reverse('cal:calendar'))
    else: 
        form = EventForm(instance=data)
    return(render(request, 'cal/event.html', {'form': form,'id':id}))
@login_required
def event_delete(request,id): 
     data = Event.objects.get(pk=id)  
     data.delete()
     return HttpResponseRedirect(reverse('cal:calendar'))