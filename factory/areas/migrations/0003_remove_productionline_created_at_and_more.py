# Generated by Django 5.1.1 on 2024-09-26 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_productionline_created_at_productionline_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productionline',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='productionline',
            name='updated_at',
        ),
    ]
