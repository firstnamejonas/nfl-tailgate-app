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

