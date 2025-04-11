from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.TextChoices):
    STUDENT = 'student', 'Student'
    ALUMNI = 'alumni', 'Alumni'
    STAFF = 'staff', 'Staff'
    PROSPECTIVE = 'prospective', 'Prospective Student'

class User(AbstractUser):
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.PROSPECTIVE
    )
    affiliated_university = models.ForeignKey(
        'universities.University',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='affiliated_users'
    )
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username