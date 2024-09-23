# Generated by Django 5.1.1 on 2024-09-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the product (must be unique).', max_length=220, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional detailed description of the product.', null=True)),
                ('short_code', models.CharField(help_text='Unique short code to identify the product.', max_length=20, unique=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='The last time the product was updated.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The time when the product was created.')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
    ]
