from django.urls import path
from core import views

urlpatterns = [path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path(' ContactUs/', views.ContactUs, name='ContuctUs'),
    path ('Gallery/', views.Gallery, name= 'Gallery'),
    path ('blogs/', views.blogs, name= 'blogs'),
    
] 



