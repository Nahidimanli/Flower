from django.urls import path
from core import views

urlpatterns = [path('', views.home, name='home'),
    path ('about',views.about, name = 'about'),
    path('contact', views.contact, name='contact'),
    path('contactUs', views.Setting, name='Setting'),
    path ('gallery', views.gallery, name= 'gallery'),
    path ('blogs', views.blogs, name= 'blogs'),
    
] 



