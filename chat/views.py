from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from chatrooms.models import Room

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=room, sender=request.user, content=content)
            return redirect('chat:chat_room', room_id=room_id)
    
    return render(request, 'chat.html', {'room': room, 'messages': messages})
