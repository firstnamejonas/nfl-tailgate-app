from django.db import models
from django.contrib.auth.models import User
from chatrooms.models import Room


class Message(models.Model):
    """
    Summary:
    Model for storing chat messages.

    Attributes:
    room (Room):
    Foreign key to the Room model, 
    indicating the room to which the message belongs.
    sender (User):
    Foreign key to the User model, indicating the sender of the message.
    content (str):
    The content of the message.
    timestamp (DateTimeField):
    The timestamp indicating when the message was created.

    Methods:
    __str__ (str): Returns a string representation of the message.
    can_edit (bool): Checks if the given user can edit the message.
    can_delete (bool): Checks if the given user can delete the message.
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the message.
        """
        return f'{self.sender.username} - {self.timestamp}'

    def can_edit(self, user):
        """
        Checks if the given user can edit the message.
        """
        return self.sender == user

    def can_delete(self, user):
        """
        Checks if the given user can delete the message.
        """
        return self.sender == user
