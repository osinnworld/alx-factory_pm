# Generated by Django 5.1.1 on 2024-09-23 12:48

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    dependencies = [
        ('areas', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='productionline',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productionline',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
