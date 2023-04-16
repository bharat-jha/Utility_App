from django.db import models
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# This is not working --- As result we are not getting link to edit 

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id))
        ret_url = "<a href="+str(url)+">" + str(self.title)+"</a>"
        print(ret_url)
        return(ret_url)
    
    
