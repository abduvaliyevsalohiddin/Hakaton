from django.db import models

from coreApp.models import CoreModel
from userApp.models import Profil


class Connection(CoreModel):
    user1 = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, related_name='startup')
    user2 = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, related_name='programmer')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user1} -> {self.user2}'
