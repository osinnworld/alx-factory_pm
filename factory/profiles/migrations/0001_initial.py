# Generated by Django 5.1.1 on 2024-09-22 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='Short biography or description of the user.', null=True)),
                ('profile_picture', models.ImageField(blank=True, help_text='Profile picture of the user.', null=True, upload_to='profile_pics/')),
                ('website', models.URLField(blank=True, help_text='Personal website or portfolio link.', max_length=220, null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Last time the profile was updated.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Time the profile was initially created.')),
                ('user', models.OneToOneField(help_text='The user to whom this profile belongs.', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-created'],
            },
        ),
    ]
