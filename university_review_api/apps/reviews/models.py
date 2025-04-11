from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    university = models.ForeignKey(
        'universities.University',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
        unique_together = ['university', 'user']  # One review per university per user
    
    def __str__(self):
        return f"{self.user.username}'s review of {self.university.name}"