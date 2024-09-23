from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220, unique=True, help_text="Name of the product (must be unique).")
    description = models.TextField(blank=True, null=True, help_text="Optional detailed description of the product.")
    short_code = models.CharField(max_length=20, unique=True, help_text="Unique short code to identify the product.")
    updated = models.DateTimeField(auto_now=True, help_text="The last time the product was updated.")
    created = models.DateTimeField(auto_now_add=True, help_text="The time when the product was created.")

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name} (Code: {self.short_code})"