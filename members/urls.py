from django.urls import path
from . import views

app_name ='members'
urlpatterns = [
    path('login_user/',views.login_user,name='login'),
     path('dashbord/', views.dashbord, name="dashbord"),
    #path('world/', views.world_view, name= 'world'),
    #path('area_form/',views.create_area, name= 'add_area'),
]