from django.forms import ModelForm
from django import forms
from .models import ConferenceRoom, Reservation
from datetime import datetime, date


def validate_date(value):
    if value < str(datetime.today()):
        raise forms.ValidationError('Present and future time1')


class ConferenceRoomAddForm(ModelForm):
    class Meta:
        model = ConferenceRoom
        fields = "__all__"


class ReservationForm(ModelForm):
    conference_room_id = forms.HiddenInput()
    date = forms.CharField(validators=[validate_date])

    class Meta:
        model = Reservation
        fields = ["date", "comment"]
