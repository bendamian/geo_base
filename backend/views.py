from django.shortcuts import render

# Create your views here.
from .models import Category,Sight,Area
from .serializers import CategorySerializer,SightSerializer,AreaSerializer
from rest_framework import generics





 
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'


class SightList(generics.ListCreateAPIView):
    queryset = Sight.objects.all()
    serializer_class = SightSerializer
    name = 'sight-list'


class SightDetail(generics.RetrieveDestroyAPIView):
    queryset = Sight.objects.all()
    serializer_class = SightSerializer
    name= 'sight-detail'




class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    name = 'area-list'