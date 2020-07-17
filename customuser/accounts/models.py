from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# USERNAME_REGEX = "^[a-zA-Z0-9.+-]*$"


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError("Enter valide email")

        if not username:
            raise ValueError("Invalid Username")

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email), username=username, password=password,
         )

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email addess",
        max_length=100,
        unique=True,
        # validators=[
        #     RegexValidator(
        #         regex=USERNAME_REGEX,
        #         message="Enter valid email address",
        #         code="invalid email",
    )
    username = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        return True

