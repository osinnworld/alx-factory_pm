from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from categories.models import Category
from products.models import Product
from areas.models import ProductionLine
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
import uuid

class Report(models.Model):
    HOUR_CHOICES = [(x, f'{x:02d}') for x in range(1, 25)]
    
    id = models.AutoField(primary_key=True)
    day = models.DateField(default=timezone.now, help_text="Date of the report.")
    start_hour = models.IntegerField(
        choices=HOUR_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(24)],
        help_text="Start hour of the production period (1-24)."
    )
    end_hour = models.IntegerField(
        choices=HOUR_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(24)],
        help_text="End hour of the production period (1-24)."
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports', help_text="User who created the report.")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reports', help_text="Product being reported on.")
    plan = models.PositiveBigIntegerField(help_text="Planned production for the day.")
    execution = models.PositiveBigIntegerField(help_text="Actual production achieved.")
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, related_name='reports', help_text="Production line used for the report.")
    updated = models.DateTimeField(auto_now=True, help_text="Last time the report was updated.")
    created = models.DateTimeField(auto_now_add=True, help_text="Time the report was initially created.")

    class Meta:
        ordering = ['-created']
        verbose_name = "Production Report"
        verbose_name_plural = "Production Reports"
        
    def get_absolute_url(self):
        return reverse('reports:report-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Report for {self.product.name} by {self.user.username} ({self.start_hour:02d}:00-{self.end_hour:02d}:00)"

    def get_efficiency(self):
        return (self.execution / self.plan) * 100 if self.plan > 0 else 0

    def get_duration(self):
        return self.end_hour - self.start_hour

class ProblemReported(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    category = models.ForeignKey('ProblemCategory', on_delete=models.CASCADE, related_name='problems')
    description = models.TextField(help_text="Description of the problem.")
    problem_id = models.CharField(max_length=12, unique=True, default=uuid.uuid4, editable=False, help_text="Unique identifier for the problem.")
    breakdown = models.PositiveIntegerField(help_text="Breakdown or severity level of the problem.")
    public = models.BooleanField(default=False, help_text="Whether the problem is visible to the public.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problems')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='NEW')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Reported Problem"
        verbose_name_plural = "Reported Problems"

    def __str__(self):
        return f"{self.category.name}: {self.description[:20]}..."

    def get_absolute_url(self):
        return reverse('reports:problem-detail', kwargs={'pk': self.pk})

class ProblemCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Problem Category"
        verbose_name_plural = "Problem Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reports:problem-category-detail', kwargs={'pk': self.pk})