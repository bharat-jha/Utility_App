from django import forms 
from .models import Note, Subject
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

# Defining the Notes forms for the analysis ................
class Notes_Form(forms.ModelForm):
    class Meta: 
        model = Note
        fields = ['Topic','Description','date_update','status','pic']  
        widget = {
            'Description': forms.Textarea(attrs={'cols': 300, 'rows': 20})
                 }
    def __init__(self, *args, **kwargs):
        super(Notes_Form, self).__init__(*args, **kwargs)
        self.fields['pic'].required = False


# Defining the subject forms for the analysis ................
class Subject_Form(forms.ModelForm):   
    class Meta:   
        model =  Subject
        fields = '__all__'
    
        
        
