from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from chatrooms.models import Team

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('image', default='https://res.cloudinary.com/dgljwtt70/image/upload/v1709640781/zazmnydazkuerafegnfk.png', blank=True, null=True)
    favorite_team = models.ForeignKey('chatrooms.Team', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username