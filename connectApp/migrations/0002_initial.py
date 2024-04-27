# Generated by Django 5.0.4 on 2024-04-26 12:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('connectApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='startup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='connection',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programmer', to=settings.AUTH_USER_MODEL),
        ),
    ]
