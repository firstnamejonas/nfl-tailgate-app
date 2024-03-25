from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import SignUpView
from django.contrib.messages import get_messages
from django.http import HttpRequest


class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('signup')

    def test_get_request_returns_signup_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_post_request_creates_user_and_redirects_to_login(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        # Check if the user is created
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Check success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your account has been created successfully. Please login.')
