from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Customer


class CustomUserAdmin(UserAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "code", "phone"]
    list_display_links = ["user", "code"]


admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
