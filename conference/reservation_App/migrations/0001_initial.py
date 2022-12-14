# Generated by Django 4.1.2 on 2022-11-15 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255, unique=True)),
                ('room_capacity', models.PositiveSmallIntegerField()),
                ('projector_availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('conference_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation_App.conferenceroom')),
            ],
            options={
                'unique_together': {('date', 'conference_room_id')},
            },
        ),
    ]
