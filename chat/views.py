from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from chatrooms.models import Room

@login_required
def chat_room(request, room_slug):
    """
    Summary:
    Renders the chat room page with messages and handles message submission.

    Parameters:
    request (HttpRequest): The HTTP request object.
    room_slug (str): The slug of the room to display.

    Returns:
    HttpResponse: The HTTP response object containing the rendered chat room page.
    """
    room = get_object_or_404(Room, slug=room_slug)
    messages = Message.objects.filter(room=room).order_by('-timestamp')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=room, sender=request.user, content=content)
            return redirect('chat:chat_room', room_slug=room_slug)

    for message in messages:
        message.editable = message.can_edit(request.user)
        message.deletable = message.can_delete(request.user)
    
    return render(request, 'chat.html', {'room': room, 'messages': messages})


@login_required
def edit_message(request, message_id):
    """
    Summary:
    Renders the message edit page and handles message editing.

    Parameters:
    request (HttpRequest): The HTTP request object.
    message_id (int): The ID of the message to edit.

    Returns:
    HttpResponse: The HTTP response object containing the rendered edit message page.
    """
    message = get_object_or_404(Message, id=message_id)
    if not message.can_edit(request.user):
        pass

    if request.method == 'POST':
        new_content = request.POST.get('content')
        if new_content:
            message.content = new_content
            message.save()
            return redirect('chat:chat_room', room_slug=message.room.slug)

    return render(request, 'edit_message.html', {'message': message})

@login_required
def delete_message(request, message_id):
    """
    Summary:
    Renders the message delete page and handles message deletion.

    Parameters:
    request (HttpRequest): The HTTP request object.
    message_id (int): The ID of the message to delete.

    Returns:
    HttpResponse: The HTTP response object containing the rendered delete message page.
    """
    message = get_object_or_404(Message, id=message_id)
    if not message.can_delete(request.user):
        pass

    if request.method == 'POST':
        message.delete()
        return redirect('chat:chat_room', room_slug=message.room.slug)

    return render(request, 'delete_message.html', {'message': message})

