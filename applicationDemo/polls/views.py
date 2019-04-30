

# Create your views here.
from datetime import date,timezone


#def currentDateTime(request):
   # timeNow=datetime.datetime.now()
   # html="<html><body>Its is now %s</body></html>" %timeNow
   # return HTTPResponse(html)
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    today = date.today()
    #vars="Hello world %s" %today
    #vars2="<html><body>Its is now %s</body></html>" %today
    #return HttpResponse(vars2)
    return render(request,'polls/index.html') 

