from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Setting, Advertisement, About, Gallery, Shop
from core.forms import ContactUsForm
from django.views.generic import ListView, DetailView
from django.utils import translation
from django.conf import settings


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

def blog(request, slug):
    blogs = Blog.objects.get(slug=slug)

    context = {
        'blogs': blogs
    }

    return render(request, "blogdetails.html", context)



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



def set_language(request):
    lang_code = request.GET.get('language')
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if lang_code in dict(settings.LANGUAGES).keys():
        print("tfgvbhjnkm")
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response


# class BlogListView(ListView):
#     model = Blog
#     template_name = 'blogs.html'
#     context_object_name = 'blogs'

#     def get_queryset(self):
#         data = Blog.objects.all()
#         return data
def shops (request):
    shops = Shop.objects.all()[:3]
    count = 3
    if request.method == 'POST':
        more = int(request.POST['more-shop'])
        shops = Shop.objects.all()[:more+3]  
        count = len(shops)
    context = {
        'shops': shops,
        'count': count,
    }
    return render(request, 'shops.html', context)