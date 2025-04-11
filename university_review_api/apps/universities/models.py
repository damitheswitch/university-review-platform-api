from django.db import models
from django.db.models import Avg

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.country})"
    
    @property
    def average_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return avg or 0