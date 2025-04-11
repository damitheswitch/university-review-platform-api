from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('alumni', 'Alumni'),
        ('staff', 'Staff'),
        ('public', 'Public'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='public')
    affiliated_university = models.ForeignKey(
        'universities.University', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='affiliated_users'
    )