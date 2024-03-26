from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from chatrooms.models import Team
from .forms import ProfilePictureForm, FavoriteTeamForm

class ProfileModelTest(TestCase):
    def test_profile_str(self):
        """
        Checks whether the string representation of the profile is correct.
        """
        user = User.objects.create(username='testuser1')
        team = Team.objects.create(name='Test Team')
        profile = user.profile
        expected_string = 'testuser1'
        self.assertEqual(str(profile), expected_string)

class ProfileViewsTest(TestCase):
    def setUp(self):
        """
        Set up a test client and create necessary objects for testing.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser2', password='password')
        self.team = Team.objects.create(name='Test Team')
        self.profile = self.user.profile

    def test_user_profile_view(self):
        """
        Test the user profile view.
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('userprofile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_user_profile_view_post(self):
        """
        Test the user profile view for POST request.
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('userprofile'), {'change_picture': '', 'picture': 'test.jpg'})
        self.assertEqual(response.status_code, 302)

class ProfileFormsTest(TestCase):
    def test_profile_picture_form(self):
        """
        Test the profile picture form.
        """
        form = ProfilePictureForm()
        self.assertFalse(form.is_valid())

    def test_favorite_team_form(self):
        """
        Test the favorite team form.
        """
        team = Team.objects.create(name='Test Team')
        data = {'favorite_team': team.id}
        form = FavoriteTeamForm(data=data)
        self.assertTrue(form.is_valid())
