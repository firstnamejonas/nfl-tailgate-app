from django.contrib.auth.models import User
from django.db import models
from rooms.models import Team

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('image', default='placeholder', blank=True, null=True)
    favorite_team = models.ForeignKey(Team, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username