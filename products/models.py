from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from core.utils import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=250)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )

    def __str__(self):
        return self.name
