from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class Sight(models.Model):
    
    class SightObjects(models.Manager):
        def get_queryset(self):
           return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='place_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    point_geom = models.PointField()
    objects = models.Manager()  # default manager
    Sightseeing = SightObjects()  # custom manager

    class Meta:
        ordering = ('-published',)
        verbose_name_plural = 'Sights'

    def __str__(self):
        return  f" {self.name},{self.city},{self.published}"



class Area(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField('location name', max_length=225, help_text=" name of the Location")
    boundary = models.PolygonField()
    image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Areas'

    def __str__(self):
        return f" {self.name},{self.city},  {self.county}"        