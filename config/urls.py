from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from frontend import views
from members.views import(login_user,dashbord,logout_user)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
    path('', include('frontend.urls', namespace='frontend_app')),
    path('world/', views.world_view, name= 'world'),
    #path('members/', include('django.contrib.auth.urls')),
    path('',login_user,name='login'),
    path('dashbord/',dashbord,name='dashbord'),
    path('members/', include('members.urls', namespace='members')),
    
      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

