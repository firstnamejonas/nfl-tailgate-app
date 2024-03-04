from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    categories = set(room.category for room in rooms)
    return render(request, 'chatrooms.html', {'rooms': rooms, 'categories': categories})
