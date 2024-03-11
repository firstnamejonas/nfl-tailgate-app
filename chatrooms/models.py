from django.db import models
from cloudinary.models import CloudinaryField

class Team(models.Model):
    """
    Summary:
    Model for representing a team.

    Attributes:
    name (str): The name of the team.
    logo (CloudinaryField): The logo of the team stored in Cloudinary.

    Methods:
    __str__ (str): Returns a string representation of the team.
    """
    name = models.CharField(max_length=100)
    logo = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

class Room(models.Model):
    """
    Summary:
    Model for representing a chat room.

    Attributes:
    name (str): The name of the chat room.
    slug (str): The slug of the chat room.
    category (str): The category of the chat room.
    team (Team): The team associated with the chat room.

    Methods:
    save: Overridden save method to generate a slug for the room if not provided.
    __str__ (str): Returns a string representation of the chat room.
    """
    CATEGORIES = (('Teams', 'Teams'), ('Fantasy Football & More', 'Fantasy Football & More'), ('Other Teams', 'Other Teams'))
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, default='')
    category = models.CharField(max_length=100, choices=CATEGORIES, null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
