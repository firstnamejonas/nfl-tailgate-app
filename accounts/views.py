from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import generic
from django.contrib import messages


class SignUpView(generic.CreateView):
    """
    Summary:
    View class for user sign-up functionality.

    Attributes:
    form_class (UserCreationForm): Form class for user creation.
    success_url (str): URL to redirect to upon successful user creation.
    template_name (str): Template file for rendering the sign-up page.

    Methods:
    form_valid (HttpResponse): Handles valid form submission, 
    displays success message and redirects user.

    """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        """
        Function to show success message on Login-Page,
        after successfull user signup!
        """
        response = super().form_valid(form)
        messages.success(self.request, 
        'Your account has been created successfully. Please login.')
        return response
