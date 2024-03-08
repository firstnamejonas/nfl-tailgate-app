from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from chatrooms.models import Room

@login_required
def chat_room(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=room, sender=request.user, content=content)
            return redirect('chat:chat_room', room_slug=room_slug)
    
    return render(request, 'chat.html', {'room': room, 'messages': messages})
