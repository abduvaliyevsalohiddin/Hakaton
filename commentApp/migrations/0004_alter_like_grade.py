# Generated by Django 5.0.4 on 2024-04-27 07:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentApp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='grade',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
