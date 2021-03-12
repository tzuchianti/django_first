from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

def all_events(request):
        event_list = Event.objects.all()
        return render(request , 'polls/event_list.html',{'event_list':event_list})
        
def home(request, year=datetime.now().year , month=datetime.now().strftime('%B')):
        name = "john"
        month = month.capitalize()
    
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)
        
        cal = HTMLCalendar().formatmonth(year, month_number)
        
        #get currnet year
        now = datetime.now()
        current_year = now.year
    
        #get current time
        time = now.strftime('%I:%M %p')
        
        return render(request,
                      'polls/home.html',{
                        'name':name,
                        'year':year,
                        'month':month,
                        'month_number':month_number,
                        'cal':cal,
                        'current_year':current_year,
                        'time':time
                      }
                      )