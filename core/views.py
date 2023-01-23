from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Setting, Advertisement

# Create your views here.

def home(request):
    my_setting = Setting.objects.first()
    advars = Advertisement.objects.all()
    context = {
        'settings': my_setting,  
        'advars' : advars 

     }
 
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')


def ContactUs(request):
    return render (request, 'contact.html')


def Gallery(request):
    return render (request, 'gallery.html')

def blogs (request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)