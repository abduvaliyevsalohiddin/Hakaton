from django.db import models

from coreApp.models import CoreModel
from mainApp.models import Project
from userApp.models import Profil


class Comment(CoreModel):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.project}"


class Like(CoreModel):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    grade = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user} - {self.project}"
