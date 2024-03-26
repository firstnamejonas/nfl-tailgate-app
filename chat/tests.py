from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from chatrooms.models import Room
from .models import Message

class MessageModelTest(TestCase):
    def setUp(self):
        """
        Sets up the environment for the tests by creating a test user, a test room, and a test message.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.room = Room.objects.create(name='Test Room', slug='test-room')
        self.message = Message.objects.create(room=self.room, sender=self.user, content='Test message')

    def test_message_str(self):
        """
        Checks if the string representation of the message is correct.
        """
        expected_string = f'{self.user.username} - {self.message.timestamp}'
        self.assertEqual(str(self.message), expected_string)

    def test_can_edit(self):
        """
        Checks if a user can edit the message.
        """
        self.assertTrue(self.message.can_edit(self.user))

    def test_can_delete(self):
        """
        Checks if a user can delete the message.
        """
        self.assertTrue(self.message.can_delete(self.user))
