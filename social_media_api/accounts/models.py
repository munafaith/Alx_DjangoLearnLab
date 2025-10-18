from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model with additional profile fields.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # 'self' creates a relationship with the same model.
    # symmetrical=False means if you follow me, I don't automatically follow you back.
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='following'
    )

    def __str__(self):
        return self.username