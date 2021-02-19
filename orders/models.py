from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save

from accounts.models import Customer
from core.utils import BaseModel, generate_unique_code
from products.models import Product


def unique_order_no():
    return generate_unique_code("order", 7)


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
    code = models.CharField(
        max_length=7, default=unique_order_no, db_index=True
    )
    status = models.CharField(
        max_length=10, choices=CHOICES, default=TYPE_CREATED
    )

    def __str__(self):
        return f"Order {self.code}"

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


def on_order_created(sender, instance, created, **kwargs):
    if created:
        print("New order created")

        # TODO
        # Implement SMS sending logic here


post_save.connect(on_order_created, sender=Order)


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
