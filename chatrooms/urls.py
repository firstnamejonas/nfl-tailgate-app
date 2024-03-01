from django.urls import path

from .views import room_list


urlpatterns = [
    path("chatrooms/", room_list.as_view(), name="chatrooms"),
]
