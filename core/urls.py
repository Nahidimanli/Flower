from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path('', views.home, name='home'),
    path ('about',views.about, name = 'about'),
    path('contact', views.my_contact, name='contact'),
    #path('contactUs', views.Setting, name='Setting'),
    #path ('gallery', views.gallery, name= 'gallery'),
    path ('gallery', views.GalleryListView.as_view(), name= 'gallerys'),
    path("blogs/<int:id>", views.blog),
    path ('blogs', views.blogs, name= 'blogs'),
   
    # path ('blogs', views.BlogListView.as_view(), name= 'blogs'),
    path ('setting', views.SettingListView.as_view(), name= 'settings')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



