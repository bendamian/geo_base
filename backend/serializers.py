from .models import Category, Sight,Area
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name')



class SightSerializer(GeoFeatureModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Sight
        geo_field = 'point_geom'
        fields = ('pk', 'category', 'name','city', 'slug')





    
    
  
class AreaSerializer(GeoFeatureModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Area
        geo_field = 'boundary'
        fields = ('pk', 'category', 'name', 'boundary','image','city','county', 'active')