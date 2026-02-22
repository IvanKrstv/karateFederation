from django.core.validators import MinLengthValidator
from django.db import models

from common.validators import OnlyLetterValidator, FileSizeValidator


# Create your models here.
class CommonInfoMixin(models.Model):
    photo = models.ImageField(
        null=True,
        blank=True,
        validators=[
            FileSizeValidator(file_size=10)
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    class Meta:
        abstract = True


class PersonInfoMixin(models.Model):
    class GendersChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=3),
            OnlyLetterValidator()
        ],
    )

    gender = models.CharField(
        max_length=6,
        choices=GendersChoices.choices,
    )
    birth_date = models.DateField()

    class Meta:
        abstract = True