from django.contrib import admin
from django.urls import path
from reservation_App.views import AddConferenceRoom, HomeView, AllRooms, DeleteRoom, EditRoom, ReservationView, RoomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name="home"),
    path('add_room/', AddConferenceRoom.as_view(), name="add_room"),
    path('all_rooms/', AllRooms.as_view(), name="all_rooms"),
    path('delete_room/<int:id>', DeleteRoom.as_view(), name="delete_room"),
    path('edit_room/<int:id>', EditRoom.as_view(), name='edit_room'),
    path('room_reserve/<int:id>', ReservationView.as_view(), name='reserve'),
    path('room/<int:id>', RoomView.as_view(), name="room")
]
