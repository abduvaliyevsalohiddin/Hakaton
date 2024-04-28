from django.db import models

from coreApp.models import CoreModel
from mainApp.models import Project
from userApp.models import Profil


class Connection(CoreModel):
    user1 = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, related_name='startup')
    user2 = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, related_name='programmer')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user1} -> {self.user2}'


class Vacancy(CoreModel):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    salary = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    soni = models.PositiveSmallIntegerField(default=1)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.project_id} -> {self.salary}'
