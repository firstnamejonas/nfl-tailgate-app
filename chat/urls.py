from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('<room_id>/', views.chat_room, name='chat_room'),
]
