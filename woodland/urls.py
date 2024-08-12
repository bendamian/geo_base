from django.urls import path
from . import views


app_name = 'wood_land'
urlpatterns = [
   
    path('woods/', views.woods_view, name='woods'),
   
]
