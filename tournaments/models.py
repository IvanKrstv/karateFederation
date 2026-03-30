from django.core.validators import MinLengthValidator
from django.db import models

from common.models import CommonInfoMixin
from common.validators import OnlyLetterValidator


# Create your models here.
class Tournament(CommonInfoMixin):
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=3)
        ],
    )

    date = models.DateField()

    country = models.CharField(
        max_length=50,
        validators=[
            OnlyLetterValidator(message="the country must include only letters!")
        ]
    )

    city = models.CharField(
        max_length=50,
        validators=[
            OnlyLetterValidator(message="the city must include only letters!")
        ]
    )

    teams = models.ManyToManyField(
        to='athletes.Team',
        related_name='tournaments'
    )

    def __str__(self):
        return self.name