from django.db import models

from accounts.models import Customer
from core.utils import BaseModel, unique_order_no


class Order(BaseModel):

    TYPE_CREATED = "created"
    TYPE_DISPATCHED = "dispatched"
    TYPE_DELIVERED = "delivered"
    TYPE_CANCELLED = "cancelled"

    CHOICES = (
        (TYPE_CREATED, "Created"),
        (TYPE_DISPATCHED, "Dispatched"),
        (TYPE_DELIVERED, "Delivered"),
        (TYPE_CANCELLED, "Cancelled"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    number = models.CharField(
        max_length=7, default=unique_order_no, db_index=True
    )
    status = models.CharField(
        max_length=10, choices=CHOICES, default=TYPE_CREATED
    )

    def __str__(self):
        return f"Order {self.number}"

    @property
    def subtotal(self):
        pass

    @property
    def vat(self):
        pass

    @property
    def amount(self):
        pass
