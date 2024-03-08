from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('<slug:room_slug>/', views.chat_room, name='chat_room'),
    path('edit/<int:message_id>/', views.edit_message, name='edit_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]
