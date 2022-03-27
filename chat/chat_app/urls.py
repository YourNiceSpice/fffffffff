from django.urls import path

from . import views


urlpatterns = [path("rooms/", views.RoomListView.as_view() ),
               path("rooms/<room_name>/", views.RoomDetailsView.as_view()),
               path("rooms/<room_name>/create/", views.MessageCreateView.as_view()),
               path("reg/", views.RegistrationView.as_view() ),
               path("create-room/", views.RoomCreateView.as_view())

               ]
