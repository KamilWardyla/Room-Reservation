from django.db import models


# Create your models here.

class ConferenceRoom(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_capacity = models.PositiveSmallIntegerField()
    projector_availability = models.BooleanField()


class Reservation(models.Model):
    date = models.DateTimeField()
    comment = models.TextField()
    conference_room_id = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'conference_room_id')
