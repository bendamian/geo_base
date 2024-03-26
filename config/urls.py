from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
     path('backend/', include('backend.urls')),
     path('', include('frontend.urls')),
     
      #path('backend/', include('djoser.urls')),
       #path('backend/', include('djoser.urls.authtoken')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
