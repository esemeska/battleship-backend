from enum import Enum
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    username = models.CharField(max_length=20, default="user_asd")
    password = models.CharField(max_length=30, default='qwerty123')

class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='stats')
    data = models.JSONField(default=dict)


class Map(models.Model):
    ships = models.JSONField(default=list)
    shots = models.JSONField(default=list)

class Match(models.Model):
    class State(Enum):
        PENDING = "pending"
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"

        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]

    status = models.CharField(max_length=20, choices=State.choices(), default=State.PENDING.value)
    moves_history = models.JSONField(default=list)


class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='players')
    player = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    player_map = models.OneToOneField(Map, on_delete=models.CASCADE, null=True, blank=True)

class Ship(models.Model):
    class ShipType(models.TextChoices):
        DESTROYER = 'destroyer', 'Destroyer'
        SUBMARINE = 'submarine', 'Submarine'
        CRUISER = 'cruiser', 'Cruiser'
        BATTLESHIP = 'battleship', 'Battleship'
        CARRIER = 'carrier', 'Carrier'

    class ShipStatus(models.TextChoices):
        INTACT = 'intact', 'Intact'
        DAMAGED = 'damaged', 'Damaged'
        DESTROYED = 'destroyed', 'Destroyed'

    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='ship_set')
    ship_type = models.CharField(max_length=10, choices=ShipType.choices, default=ShipType.DESTROYER)
    status = models.CharField(max_length=9, choices=ShipStatus.choices, default=ShipStatus.INTACT)
    position = models.JSONField(default=list)