from django.contrib.auth.models import AbstractUser
from django.db import models

from coreApp.models import CoreModel

ROLE_CHOICES = (
    ('programmer', 'programmer'),
    ('startup', 'startup'),
)

GENDER_CHOICES = (
    ('erkak', 'erkak'),
    ('ayol', 'ayol')
)


class Profil(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profil_image = models.ImageField(upload_to='profil_image', blank=True, null=True)

    def __str__(self):
        return f'{self.username} {self.phone_number}'
