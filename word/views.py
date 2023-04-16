from django.shortcuts import render
from .forms import WordForm
from django.contrib import messages
from .models import Word,Vocab
from django.http import HttpResponseRedirect
import requests
import json 
from datetime import date 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
import json 
import requests

# getting city name from the IP address 
def ipInfo(addr=''):
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    city = data['city']
    country = data['country']
    if country=='IN':
        country = 'India'
    return(city,country)

URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

# Getting the word which we got from dictionary API #
def get_data(word=None):
    URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + str(word)
    r = requests.get(url=URL)
    msg = r.json()
    print(msg)
    definition =msg[0]['meanings'][0]
    defintions = definition.get('definitions')
    de=""
    i = 0
    for k in defintions:
        de =  de  + str(i+1)+ ".)"+ k['definition'] + ";"
        i= i+1
    return(de)

# Top Business Headlines of the day ....
def newsheadline(contry='in',category='business'):
    news = []

    url = 'https://newsapi.org/v2/top-headlines?country=in&category='+category+'&apiKey=26f18f08ef6945bf92950781cb67bc3e'
    response = requests.get(url)
    news_dict = response.json()['articles'][2:12]
 
    i = 1
    for new in news_dict:
        news.append([new['title'],new['url']])
 
        i= i+1 

    return(news)

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        fm = WordForm(request.POST)
        if fm.is_valid():
            word1 = fm.cleaned_data['word']
            request.session['word'] = word1
            data = Word(word=word1)
            data.save()
            return HttpResponseRedirect('/search/')
    else:
        fm = WordForm()  
    return(render(request,'word/home.html',{'fm':fm}))

@login_required
def search(request):
    api ="https://api.dictionaryapi.dev/api/v2/entries/en/"
    word = request.session.get('word')
    todays_date = date.today()
    msg = get_data(word)
    usr =  request.user.username
    search_dt = date( date.today().year,date.today().month ,date.today().day)
    data = Vocab(user=request.user,word=word,meaning=msg,search_dt=search_dt )
    data.save()
    messages.success(request,'Word has been stored in your Profile!!')
    return(render(request,'word/meaning.html',{'meaning': msg,'word':word }))


@login_required
def word_list(request):
    user = request.user
    words = Vocab.objects.filter(user_id = user)
    return(render(request,'', {'words': words}))

@login_required
def dashboard(request):
    words = Vocab.objects.filter(user_id = request.user).order_by('-search_dt')[:5]
 
    city,country = ipInfo()

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+str(city) +'&units=metric&APPID=8b3e4d8fed51d39bcae7a655315a5f4f')
    weather_dict = r.json() 
    news =  newsheadline(contry=country,category='sport')

    humidity = weather_dict['main']['humidity']
    feels_like = weather_dict['main']['feels_like']
    temp_max =  weather_dict['main']['temp_max']
    temp_min =  weather_dict['main']['temp_min']
    temp =   weather_dict['main']['temp']
    wind_direction = weather_dict['wind']['speed']
    context = {
        "welcome": "Welcome to your DashBoard..",
        'words':words,
        'city': city,
        'country': country,
        'temp_max' : temp_max,
        'temp_min' :temp_min ,
        'current_temp': temp,
        'wind_direction': wind_direction,
        'humidity': humidity,
        'news':news
    }
    return render(request, 'word/dashboard.html', context=context)
