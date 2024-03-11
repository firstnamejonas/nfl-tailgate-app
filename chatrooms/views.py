from django.shortcuts import render
from .models import Room
from userprofile.models import Profile

def room_list(request):
    """
    Summary:
    Renders the room list page with chat rooms and categories.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The HTTP response object containing the rendered room list page.
    """
    rooms = Room.objects.all()
    categories = set(room.category for room in rooms)
    profile = Profile.objects.get(user=request.user)
    return render(request, 'chatrooms.html', {'rooms': rooms, 'categories': categories, 'profile': profile})
