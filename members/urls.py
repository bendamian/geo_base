from django.urls import path
from . import views

app_name ='members'
urlpatterns = [
    path('login_user/',views.login_user,name='login'),
#   path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup, name="signup"),
    path('logout/',views.logout_user, name='logout'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    
    #path('world/', views.world_view, name= 'world'),
    #path('area_form/',views.create_area, name= 'add_area'),
]