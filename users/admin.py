from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "user_name",
        "nickname",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_filter = ["is_active", "is_staff", "is_superuser"]

    class Meta:
        model = User
