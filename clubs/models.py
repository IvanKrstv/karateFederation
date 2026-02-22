from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from common.models import CommonInfoMixin
from common.validators import OnlyLetterValidator


# Create your models here.
class Club(CommonInfoMixin):
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=3)
        ],
    )

    founder_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=3),
            OnlyLetterValidator()
        ]
    )

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

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.city}")
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'city'],
                name='unique_club_name_city'
            )
        ]