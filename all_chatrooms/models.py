from django.db import models

# Create your models here.

from django.db import models

class Room(models.Model):
    chatroom_title = models.CharField(max_length=100, unique=True)
    chatroom_image = models.ImageField(upload_to='room_images', null=True, blank=True)

    def __str__(self):
        return self.chatroom_title
