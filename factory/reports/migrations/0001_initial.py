# Generated by Django 5.1.1 on 2024-09-22 17:42

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('categories', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.DateField(default=django.utils.timezone.now, help_text='Date of the report.')),
                ('start_hour', models.IntegerField(choices=[(1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24')], help_text='Start hour of the production period (1-24).', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)])),
                ('end_hour', models.IntegerField(choices=[(1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24')], help_text='End hour of the production period (1-24).', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)])),
                ('plan', models.PositiveBigIntegerField(help_text='Planned production for the day.')),
                ('execution', models.PositiveBigIntegerField(help_text='Actual production achieved.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Last time the report was updated.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Time the report was initially created.')),
                ('product', models.ForeignKey(help_text='Product being reported on.', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='products.product')),
                ('production_line', models.ForeignKey(help_text='Production line used for the report.', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='areas.productionline')),
                ('user', models.ForeignKey(help_text='User who created the report.', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Production Report',
                'verbose_name_plural': 'Production Reports',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ProblemReported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Description of the problem.')),
                ('problem_id', models.CharField(help_text='Unique identifier for the problem.', max_length=12, unique=True)),
                ('breakdown', models.PositiveIntegerField(help_text='Breakdown or severity level of the problem.')),
                ('public', models.BooleanField(default=False, help_text='Whether the problem is visible to the public.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Last time the problem report was updated.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Time the problem report was initially created.')),
                ('category', models.ForeignKey(help_text='Category of the reported problem.', on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='categories.category')),
                ('user', models.ForeignKey(help_text='User who reported the problem.', on_delete=django.db.models.deletion.CASCADE, related_name='problems', to=settings.AUTH_USER_MODEL)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.report')),
            ],
            options={
                'verbose_name': 'Reported Problem',
                'verbose_name_plural': 'Reported Problems',
                'ordering': ['-created'],
            },
        ),
    ]
