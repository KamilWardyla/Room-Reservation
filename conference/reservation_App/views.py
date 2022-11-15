from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import ConferenceRoomAddForm, ReservationForm
from .models import ConferenceRoom, Reservation
from datetime import datetime


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


class AddConferenceRoom(View):
    def get(self, request):
        form = ConferenceRoomAddForm()
        ctx = {"form": form}
        return render(request, "add_conference.html", ctx)

    def post(self, request):
        form = ConferenceRoomAddForm(request.POST)
        ctx = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("all_rooms")
        return render(request, "add_conference.html", ctx)


class AllRooms(View):
    def get(self, request):
        all_rooms = ConferenceRoom.objects.all()
        reservation = Reservation.objects.all().order_by('-date')
        date_time_now = datetime.today()
        ctx = {"all_rooms": all_rooms, "date_time_now": date_time_now, "reservation": reservation}
        return render(request, 'all_rooms.html', ctx)


class DeleteRoom(View):
    def get(self, request, id):
        room = get_object_or_404(ConferenceRoom, pk=id)
        return render(request, "delete_room.html", {"room": room})

    def post(self, request, id):
        room = get_object_or_404(ConferenceRoom, pk=id)
        if room:
            room.delete()
            return redirect('all_rooms')
        return render(request, "delete_room.html", {"room": room})


class EditRoom(View):
    def get(self, request, id):
        room = get_object_or_404(ConferenceRoom, pk=id)
        form = ConferenceRoomAddForm(instance=room)
        ctx = {"form": form, "room": room}
        return render(request, "edit_room.html", ctx)

    def post(self, request, id):
        room = get_object_or_404(ConferenceRoom, pk=id)
        form = ConferenceRoomAddForm(request.POST, instance=room)
        ctx = {"form": form, "room": room}
        if form.is_valid():
            form.save()
            return redirect('all_rooms')
        return render(request, 'edit_room.html', ctx)


class ReservationView(View):
    def get(self, request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        form = ReservationForm()
        ctx = {"form": form, "room": room}
        return render(request, "reserve.html", ctx)

    def post(self, request, id):
        room = get_object_or_404(ConferenceRoom, id=id)
        form = ReservationForm(request.POST, instance=room)
        date = request.POST.get('date')
        comment = request.POST.get('comment')
        ctx = {"room": room, "form": form}
        if form.is_valid():
            Reservation.objects.create(conference_room_id=room, date=date, comment=comment)
            return redirect('all_rooms')
        return render(request, "reserve.html", ctx)


class RoomView(View):
    def get(self, request, id):
        room = get_object_or_404(ConferenceRoom, pk=id)
        reservation = Reservation.objects.all().filter(conference_room_id=id).order_by('-date')
        ctx = {"room": room, "reservation": reservation}
        return render(request, 'room.html', ctx)
