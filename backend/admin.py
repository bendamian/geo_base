from django.contrib.gis import admin
from .models import Category,Sight

# Register your models here.

admin.site.register(Category)



class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 4,
            'default_longitude': 51.509865,
            'default_latitude': -0.118092
        }

    }


@admin.register(Sight)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "city",'published')





