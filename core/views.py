from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Setting, Advertisement, About, Gallery, Shop, Catagory, tutorial
from core.forms import ContactUsForm
# from django.views.generic import ListView, DetailView
from django.utils import translation
from django.conf import settings
from django.db.models.query_utils import Q
from django.db.models import QuerySet, Avg, Q, Count


# Create your views here.

def home(request):
    settings = Setting.objects.all()
    advars = Advertisement.objects.all()
    blogs=Blog.objects.all()
    shops=Shop.objects.all()
    
    context = {
        'settings': settings,  
        'advars' : advars,
        'blogs' : blogs[0:3],
        'shops' : shops[0:3],
    }
 
    return render(request, 'index.html', context)

def about(request):
     abouts = About.objects.all()
     context = {
        'abouts' : abouts
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
 
def gallery(request):
    Tut = tutorial.objects.all()

    context = {
        'Tut': Tut
    }

	

    return render(request, 'gallery.html',context)


def  gallery_details(request,pk):
	Tut = tutorial.objects.get(pk=pk)
	context = {
	'Tut': Tut,
	}
	return  render(request, 'gallery_details.html', context)









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


# class GalleryListView(ListView):
#     model = Gallery
#     template_name = 'gallery.html'
#     context_object_name = 'gallerys'

#     def get_queryset(self):
#         data = Gallery.objects.all()
#         return data



# class SettingListView(ListView):
#     model = Setting
#     template_name = '_footer.html'
#     context_object_name = 'settings'

#     def get_queryset(self):
#         data = Setting.objects.all()
#         return data



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
def search_shop(query) -> QuerySet:
    return Shop.objects.filter(title__icontains = query)

def shop_search(request):
	
	query = request.GET["query"]

	shops = Shop.objects.filter(title__icontains = query)
    

	context = {'shops':shops, 'blogs': blogs , }

	return render(request, 'search.html', context)

def shops (request):
    shops = Shop.objects.all()[:3]
    count = 3
    catagorys = Catagory.objects.all()

    if "catagory" in request.GET.keys():
        print(request.GET["catagory"])
        shops = Shop.objects.filter(
            catagory_id__name=request.GET["catagory"])
    if request.method == 'POST':
        more = int(request.POST['more-shop'])
        shops = Shop.objects.all()[:more+3]  
        count = len(shops)
    context = {
        'shops': shops,
        'count': count,
        'catagorys': catagorys,
    }
    return render(request, 'shops.html', context)


def shop_search(request):
	
	query = request.GET["query"]

	shops = Shop.objects.filter(title__icontains=query)
    

	context = {'shops':shops, 'blogs': blogs , }

	return render(request, 'search.html', context)


def shop(request, slug):
    shops = Shop.objects.get(slug=slug)

    context = {
        'shops': shops
    }

    return render(request, "shop_details.html", context)