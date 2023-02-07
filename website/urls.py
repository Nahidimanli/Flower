"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from baseuser.views import register,login
from django.contrib import admin
from django.urls import path
from core.views import home, GalleryListView
from django.conf import settings
from django.conf.urls.static import static
from core.urls import urlpatterns as core_urls
from django.conf.urls import include
from baseuser.urls import ulpatterns as baseuser_urls
#from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('baseuser/', include(baseuser_urls)),
    path('', include('social_django.urls', namespace='social')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    