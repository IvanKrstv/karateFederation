from django.db import models

from common.models import CommonInfoMixin, PersonInfoMixin


# Create your models here.
class Coach(PersonInfoMixin, CommonInfoMixin):
    class CoachLicenseChoices(models.TextChoices):
        A = 'A', 'A'
        B = 'B', 'B'
        C = 'C', 'C'
        D = 'D', 'D'

    coach_license = models.CharField(
        max_length=1,
        choices=CoachLicenseChoices, # .choices?
        default=CoachLicenseChoices.D
    )

    # Many-to-one relation to the club model, many coaches can be in one club
    club = models.ForeignKey(
        to='clubs.Club',
        on_delete=models.CASCADE,
        related_name='coaches'
    )