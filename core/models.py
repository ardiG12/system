from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Rank(models.TextChoices):
        E = "E", "E"
        D = "D", "D"
        C = "C", "C"
        B = "B", "B"
        A = "A", "A"
        S = "S", "S"

    rank = models.CharField(
        max_length=1,
        choices=Rank.choices,
        default=Rank.E,
    )
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)

    # статы
    strength = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    endurance = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
