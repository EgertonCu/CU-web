from django.shortcuts import render
from .models import *

# Create your views here.
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
    return render(request, 'website/gallery.html')

def library(request):
    return render(request, 'website/E-Library.html')

def contact(request):
    return render(request, 'website/contact.html')

def blogsingle(request):
    return render(request, 'website/blog-single.html')
