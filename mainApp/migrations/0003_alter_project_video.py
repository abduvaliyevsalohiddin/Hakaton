# Generated by Django 5.0.4 on 2024-04-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
