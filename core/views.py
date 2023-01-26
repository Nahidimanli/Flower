from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Setting, Advertisement,About,Gallery

# Create your views here.

def home(request):
    my_setting = Setting.objects.all()
    advars = Advertisement.objects.all()
    context = {
        'settings': my_setting,  
        'advars' : advars 

    }
 
    return render(request, 'index.html', context)

def about(request):
     about = About.objects.all()
     context = {
        'about' : about
     }
     return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')


def ContactUs(request):
    return render (request, 'contact.html')


def gallery(request):
     gallery = Gallery.objects.all()
     context = {
        'gallery': gallery
     }
     return render(request, 'gallery.html',context)

def blogs (request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)