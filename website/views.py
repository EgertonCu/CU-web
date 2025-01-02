from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from nltk.sentiment import SentimentIntensityAnalyzer
from django.utils.timezone import now
# Create your views here.
import nltk
nltk.download('vader_lexicon')

def homepage(request):
    events = Event.objects.all()
    testimonies = Testimony.objects.all()
    context = {
        'events': events,
        'testimonies': testimonies,
    }
    return render(request, 'website/index.html', context)

def leadership(request):
    leaders = Leader.objects.all()
    context = {
    'leaders': leaders,
    }
    return render(request, 'website/Leadership.html', context)

def ministries(request):
    eteams = Eteam.objects.all()
    ministries = Ministry.objects.all()
    context = {
        'ministries': ministries,
        'eteams': eteams,
    }
    return render(request, 'website/Ministries.html', context)

def about(request):
    return render(request, 'website/about.html')

def gallery(request):
    images = Image.objects.all()
    context = {
    'images': images,
    }
    return render(request, 'website/gallery.html', context)

def library(request):
    return render(request, 'website/E-Library.html')

def contact(request):
    return render(request, 'website/contact.html')

# def blogsingle(request):
#     return render(request, 'website/blog-single.html')

def registration(request):
    return render(request, "website/Membership_Reg.html")
