from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from .models import Room, Team
from .views import room_list

class RoomModelTest(TestCase):
    def setUp(self):
        """
        Sets up the environment for the tests by creating test objects.
        """
        self.team = Team.objects.create(name='Test Team')
        self.room = Room.objects.create(name='Test Room', slug='test-room', category='Teams', team=self.team)

    def test_room_str(self):
        """
        Checks if the string representation of the room is correct.
        """
        expected_string = 'Test Room'
        self.assertEqual(str(self.room), expected_string)

    def test_room_save(self):
        """
        Checks if the room slug is generated correctly when saving.
        """
        self.assertEqual(self.room.slug, 'test-room')  # Ensure slug is initially set
        self.room.save()  # Trigger save method to generate slug
        self.assertNotEqual(self.room.slug, '')  # Ensure slug is not empty after save

