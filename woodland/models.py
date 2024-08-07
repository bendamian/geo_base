from django.db import models

# Create your models here.


class Woodland(models.Model):
    CATEGORY_CHOICES = (
        ('Insects', 'Insects'),
        ('Plants', 'Plants'),
        ('Birds', 'Birds'),
        ('Animal', 'Animals'),

    )

    name = models.CharField(max_length=100)
    count = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Woodlands'

    def __str__(self):
        return f"{self.name} ({self.category})"