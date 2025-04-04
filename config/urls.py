from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from frontend import views
from members.views import(login_user,logout_user)
from dashboard.views import (dashboard)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
    path('', include('frontend.urls', namespace='frontend_app')),
    path('', login_user, name='login'),
    path('dashboard/', include('dashboard.urls',namespace='dashboard_app')),
    path('world/', views.world_view, name= 'world'),
    #path('members/', include('django.contrib.auth.urls')),   
    #path('dashboard/',dashboard,name='dashboard_app'),
    path('members/', include('members.urls', namespace='members')),
    path('woodland/', include('woodland.urls',namespace='wood_land')),
    
      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

