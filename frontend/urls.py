from django.urls import path
from . import views

app_name ='frontend_app'
urlpatterns = [
    path('', views.home_view, name= 'home'),
      path('world/', views.world_view, name= 'world'),
]