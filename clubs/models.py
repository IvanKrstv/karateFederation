from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from common.models import CommonInfoMixin


# Create your models here.
class Club(CommonInfoMixin):
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=3)
        ],
        unique=True
    )

    founder_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=3)
        ]
    )

    country = models.CharField(
        max_length=50
    )

    city = models.CharField(
        max_length=50
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.city}")
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name