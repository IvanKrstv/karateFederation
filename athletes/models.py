from django.db import models

from common.models import PersonInfoMixin, CommonInfoMixin


# Create your models here.
class Athlete(PersonInfoMixin, CommonInfoMixin):
    class BeltChoices(models.TextChoices):
        WHITE = 'White', 'White'
        YELLOW = 'Yellow', 'Yellow'
        ORANGE = 'Orange', 'Orange'
        GREEN = 'Green', 'Green'
        BLUE = 'Blue', 'Blue'
        BROWN = 'Brown', 'Brown'
        BLACK = 'Black', 'Black'

    belt = models.CharField(
        max_length=15,
        choices=BeltChoices.choices
    )

    club = models.ForeignKey(
        to='clubs.Club',
        on_delete=models.CASCADE,
        related_name='athletes'
    )


class Team(models.Model):
    name = models.CharField(
        max_length=50
    )

    # Many teams can be in one club
    club = models.ForeignKey(
        to='clubs.Club',
        on_delete=models.CASCADE,
        related_name='teams'
    )

    # Many athletes can participate in many clubs
    athletes = models.ManyToManyField(
        to='Athlete',
        related_name='teams'
    )
