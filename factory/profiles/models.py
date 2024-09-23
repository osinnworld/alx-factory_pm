from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', help_text="The user to whom this profile belongs.")
    bio = models.TextField(blank=True, null=True, help_text="Short biography or description of the user.")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, help_text="Profile picture of the user.")
    website = models.URLField(max_length=220, blank=True, null=True, help_text="Personal website or portfolio link.")
    updated = models.DateTimeField(auto_now=True, help_text="Last time the profile was updated.")
    created = models.DateTimeField(auto_now_add=True, help_text="Time the profile was initially created.")

    class Meta:
        ordering = ['-created']
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"Profile of {self.user.username}"