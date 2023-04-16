from django import forms 
from .models import Word

# Creating word form for the analysis....

class WordForm(forms.Form):
    word = forms.CharField(max_length=100)
    
    
class CountryForm(forms.Form):
    country_cd = forms.CharField(max_length=100)
    category_cd = forms.CharField(max_length=100)