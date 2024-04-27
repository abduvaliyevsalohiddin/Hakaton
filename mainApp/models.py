from django.db import models

from coreApp.models import CoreModel
from userApp.models import Profil


class Category(CoreModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(CoreModel):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    video = models.FileField(upload_to='project_video', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
