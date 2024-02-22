from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'user_auth/signup.html')

def login_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'user_auth/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')