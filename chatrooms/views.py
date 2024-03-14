from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from userprofile.models import Profile


@login_required
def room_list(request):
    """
    Summary:
    Renders the room list page with chat rooms and categories.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse:
    The HTTP response object containing the rendered room list page.
    """
    profile = Profile.objects.get(user=request.user)
    favorite_team = profile.favorite_team
    rooms = Room.objects.all()

    favorite_room = None
    other_rooms = []
    for room in rooms:
        if room.team == favorite_team:
            favorite_room = room
        else:
            other_rooms.append(room)

    categories = set(room.category for room in other_rooms)
    return render(request, 'chatrooms.html', {'favorite_room': favorite_room,
                                              'other_rooms': other_rooms,
                                              'categories': categories,
                                              'profile': profile})
