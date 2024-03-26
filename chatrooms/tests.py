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
        self.room = Room.objects.create(
            name='Test Room',
            slug='test-room',
            category='Teams',
            team=self.team
        )

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
        self.assertEqual(self.room.slug, 'test-room')
        self.room.save()
        self.assertNotEqual(self.room.slug, '')


class RoomViewsTest(TestCase):
    def setUp(self):
        """
        Set up a test user.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_room_list_view(self):
        """
        Test the room list view.
        """
        request = self.factory.get('/')
        request.user = self.user
        response = room_list(request)
        self.assertEqual(response.status_code, 200)

    def test_room_list_view_anonymous(self):
        """
        Test the room list view for anonymous user.
        """
        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = room_list(request)
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_room_list_view_with_parameters(self):
        """
        Test the room list view with specific parameters.
        """
        request = self.factory.get('/?category=Teams')
        request.user = self.user
        response = room_list(request)
        self.assertEqual(response.status_code, 200)
