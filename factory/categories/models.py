from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the category (must be unique).")
    description = models.TextField(blank=True, help_text="Optional description of the category.")
    updated = models.DateTimeField(auto_now=True, help_text="The last time the category was updated.")
    created = models.DateTimeField(auto_now_add=True, help_text="The time when the category was created.")

    class Meta:
        ordering = ['name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name