from django.db import models
from django.db.models import Avg

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    
    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    def __str__(self):
        return f"{self.name} ({self.country})"
    
    class Meta:
        verbose_name_plural = "Universities"
        ordering = ['name']