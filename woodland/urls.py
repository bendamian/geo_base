from django.urls import path
from . import views


app_name = 'wood_land'
urlpatterns = [
   
    path('woods/', views.woods_view, name='woods'),
    path('woods/delete/<int:pk>/', views.species_delete, name='remove_species'),
    path('woods/update/<int:pk>/', views.update_species, name='update_species'),
   
]
