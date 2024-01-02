from django.contrib import admin

# Register your models here.
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "password",
        "is_staff",
        "is_active",
        "is_superuser",
    )

admin.site.register(Account, AccountAdmin)

