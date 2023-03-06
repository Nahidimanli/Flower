from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path('', views.home, name='home'),
    path ('about',views.about, name = 'about'),
    path('contact', views.my_contact, name='contact'),
    #path('contactUs', views.Setting, name='Setting'),
    path ('gallery', views.gallery, name= 'gallerys'),
    # path ('gallery', views.GalleryListView.as_view(), name= 'gallerys'),
    path("blogs/<slug:slug>", views.blog),
    path ('blogs', views.blogs, name= 'blogs'),
    path("shops/<slug:slug>", views.shop),
    path('gallery/<int:pk>/', views.gallery_details, name='gallery_detail'),
   
    # path ('blogs', views.BlogListView.as_view(), name= 'blogs'),
    # path('setting', views.SettingListView.as_view(), name= 'settings'),
    path('set_language', views.set_language, name='set_language'),
    path ('shops', views.shops, name= 'shops'),
    path ('search', views.shop_search, name= 'search'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



