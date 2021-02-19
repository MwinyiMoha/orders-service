from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from accounts.models import Customer
from core.utils import BaseModel, unique_order_no
from products.models import Product


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
    def order_info(self):
        subtotal = sum(self.orderitem_set.values_list("item_total", flat=True))
        vat = subtotal * Decimal("0.16")
        shipping = (subtotal + vat) * Decimal("0.15")
        total = subtotal + vat + shipping

        return {
            "subtotal": subtotal,
            "vat": vat,
            "shipping": shipping,
            "total": total,
        }

    @property
    def items(self):
        return self.orderitem_set.all()


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    item_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )

    def __str__(self):
        return f"Item: {self.quantity} * {self.product}"

    def save(self, *args, **kwargs):
        self.item_total = self.quantity * self.product.price

        super(OrderItem, self).save(*args, **kwargs)
