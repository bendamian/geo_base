from django.urls import path
from . import views

app_name ='frontend_app'
urlpatterns = [
    path('', views.home_view, name= 'home'),
    path('world/', views.world_view, name= 'world'),
    path('area_form/',views.create_area, name= 'add_area'),
]