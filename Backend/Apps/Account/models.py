from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from .management.manage import AccountManager

# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, blank=True)
    password = models.CharField(max_length=256)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = AccountManager()

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return True
