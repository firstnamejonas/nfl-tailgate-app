from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from chatrooms.models import Team


class Profile(models.Model):
    """
    Summary:
    Model for storing user profiles.

    Attributes:
    user (User): One-to-One relationship with the User model.
    picture (CloudinaryField): Profile picture stored in Cloudinary.
    favorite_team (Team): The user's favorite team, if set.

    Methods:
    __str__ (str): Returns a string representation of the profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = CloudinaryField('image', default='https://res.cloudinary.com/dgljwtt70/image/upload/v1709640781/zazmnydazkuerafegnfk.png', blank=True, null=True)
    favorite_team = models.ForeignKey('chatrooms.Team',
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True)

    def __str__(self):
        return self.user.username
