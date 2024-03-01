from django.db import models
from cloudinary.models import CloudinaryField

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

class Room(models.Model):
    CATEGORIES = (('Teams', 'Teams'), ('Fantasy Football & More', 'Fantasy Football & More'), ('Other Teams', 'Other Teams'))
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORIES, null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
