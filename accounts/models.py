import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

from core.utils import BaseModel, unique_code


class User(AbstractUser):

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        name_str = self.email.split("@")[0]

        if self.first_name and self.last_name:
            name_str = self.get_full_name()

        self.username = slugify(name_str)
        super(User, self).save(*args, **kwargs)


class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    code = models.CharField(
        unique=True, db_index=True, max_length=5, default=unique_code
    )
    phone = models.CharField(max_length=12, default="254")

    def __str__(self):
        return f"customer {self.user}"


def on_user_created(sender, instance, created, **kwargs):
    if created:
        c = Customer()
        c.user = instance
        c.save()


post_save.connect(on_user_created, sender=User)
