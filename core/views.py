from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Setting, Advertisement,About,Gallery
from core.forms import ContactUsForm
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    #my_setting = Setting.objects.all()
    advars = Advertisement.objects.all()
    
    context = {
        #'settings': my_setting,  
        'advars' : advars,
    }
 
    return render(request, 'index.html', context)

def about(request):
     about = About.objects.all()
     context = {
        'about' : about
     }
     return render(request, 'about.html', context)



def my_contact(request):
    contact_model = ContactUsForm()
    if request.method == 'POST':
        contact_model = ContactUsForm(request.POST)
        if contact_model.is_valid():
            contact_model.save()
            contact_model = ContactUsForm()

    context = {
        'contactus_form' : contact_model,
    }
    return render(request, 'contact.html', context)





  
# def ContactUs(request):
#       return render(request, 'contact.html')
 
# def gallery(request):
#      gallery = Gallery.objects.all()
#      context = {
#         'gallery': gallery
#      }
#      return render(request, 'gallery.html',context)


def blogs (request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)


class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'gallerys'

    def get_queryset(self):
        data = Gallery.objects.all()
        return data



class SettingListView(ListView):
    model = Setting
    template_name = '_footer.html'
    context_object_name = 'settings'

    def get_queryset(self):
        data = Setting.objects.all()
        return data