from django.contrib.gis import forms
from backend.models import Category,Sight,Area

class AreaForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Area
        fields = ['category', 'name', 'boundary', 'image', 'city', 'county', 'active']
        labels = {
            'category': 'Category',
            'name': 'Location Name',
            'boundary': 'Boundary',
            'image': 'Image',
            'city': 'City',
            'county': 'County',
            'active': 'Active'
        }
        help_texts = {
            'name': 'Name of the Location',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.TextInput(attrs={'class': 'form-control'}),
            'boundary':  forms.OSMWidget( attrs={'map_width': 800, 'map_height': 500, 'default_lat': 51.509865, 'default_lon': -0.118092,'default_zoom': 4}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
