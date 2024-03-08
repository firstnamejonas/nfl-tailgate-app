from django.shortcuts import render
from .models import Room
from userprofile.models import Profile

def room_list(request):
    rooms = Room.objects.all()
    categories = set(room.category for room in rooms)
    profile = Profile.objects.get(user=request.user)
    return render(request, 'chatrooms.html', {'rooms': rooms, 'categories': categories, 'profile': profile})
