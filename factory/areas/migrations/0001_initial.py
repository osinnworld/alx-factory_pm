# Generated by Django 5.1.1 on 2024-09-22 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the production line (must be unique).', max_length=120, unique=True)),
                ('products', models.ManyToManyField(help_text='Products associated with this production line.', related_name='production_lines', to='products.product')),
                ('team_leader', models.ForeignKey(help_text='Profile of the team leader managing this production line.', on_delete=django.db.models.deletion.CASCADE, related_name='production_lines', to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Production Line',
                'verbose_name_plural': 'Production Lines',
                'ordering': ['name'],
            },
        ),
    ]
