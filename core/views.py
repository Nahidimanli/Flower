from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Setting, Advertisement,About,Gallery
from core.forms import ContactUsForm

# Create your views here.

def home(request):
    my_setting = Setting.objects.all()
    advars = Advertisement.objects.all()
    
    context = {
        'settings': my_setting,  
        'advars' : advars,
        

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
    contactus_form = ContactUsForm()
    if request.method =='POST':
        contactus_form ==ContactUsForm(request.POST)
    if contactus_form.is_valid():
        contactus_form.save()
        contactus_form = ContactUsForm()

    context = {
        'contactus_form' : contactus_form
    }
    return render (request, 'contact.html', context)


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