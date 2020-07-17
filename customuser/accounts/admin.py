from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm

from accounts.models import Account


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = (
        "username",
        "email",
        "is_admin",
        "is_staff",
    )
    list_filter = ("is_admin",)

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permission", {"fields": ("is_admin", "is_staff", "is_superuser",)}),
    )

    search_fields = ("username", "email")
    ordering = ("username", "email")

    filter_horizontal = ()


admin.site.register(Account, UserAdmin)

admin.site.unregister(Group)

