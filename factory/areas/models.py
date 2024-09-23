from django.db import models
from profiles.models import Profile
from products.models import Product

# Create your models here.
class ProductionLine(models.Model):
    name = models.CharField(max_length=120, unique=True, help_text="Name of the production line (must be unique).")
    team_leader = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='production_lines', help_text="Profile of the team leader managing this production line.")
    products = models.ManyToManyField(Product, related_name='production_lines', help_text="Products associated with this production line.")
    
    class Meta:
        ordering = ['name']
        verbose_name = "Production Line"
        verbose_name_plural = "Production Lines"

    def __str__(self):
        return f"{self.name} (Leader: {self.team_leader.user.username})" 