from django.shortcuts import render
from app.models import *
from app.forms import *

# Create your views here.
def Insert_topics(request):
    TOP=Topic()
    d={'top':TOP}
    if request.method=='POST':
        TP=Topic(request.POST)
        if TP.is_valid():
            Topic_names=TP.cleaned_data ['Topic_names']
            TD=Topics.objects.get_or_create(Topic_name=Topic_names)[0]
            TD.save()
            SQ=Topics.objects.all()
            d1={'TD':SQ}
            return render(request,'display_topics.html',d1)
    return render(request,'Insert_topics.html',d)


def Insert_webpage(request):
    WOP=Webpage()
    d={'wop':WOP}
    return render(request,'Insert_webpage.html',d)
    
