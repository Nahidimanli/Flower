
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
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from core.api.urls import ulpatterns as core_api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('social_django.urls', namespace='social')),
    path('core/ api/', include(core_api_urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('baseuser/', include(baseuser_urls)),
    path('', include(core_urls)),
    path('rosetta/', include('rosetta.urls')),
    
)
    