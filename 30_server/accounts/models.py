from core.constants import RoleCode
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Role(BaseModel):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "role"


class UserManager(BaseUserManager):
    def create_user(self, name: str, email: str, password: str, **extra_fields):
        # Customerロールで作成し、後からStaffに付け替える運用をする
        role = Role.objects.get(code=RoleCode.CUSTOMER)
        user: User = self.model(
            role=role, name=name, email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save()
        return user


class User(BaseModel, AbstractBaseUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "user"
