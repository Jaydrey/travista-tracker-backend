from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils.translation import gettext_lazy as text_lazy
# Create your models here.

# helper functions
def user_directory_path(instance, filename:str):
    return f"user_{instance.id}/img/{filename}"

# custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Super User should be staff member")
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Super User should be superuser")

        return self.create_user(email=email,password=password, **kwargs)

# Create your models here.
class User(AbstractUser):
    class UserType(models.TextChoices):
        SHOPKEEPER = "SK", text_lazy("ShopKeeper")
        SUPPLIER = "SP", text_lazy("Supplier")

    class Rating(models.TextChoices):
        ZERO = "0", text_lazy("0")
        ONE = "1", text_lazy("1")
        TWO = "2", text_lazy("2")
        THREE = "3", text_lazy("3")
        FOUR = "4", text_lazy("4")
        FIVE = "5", text_lazy("5")

    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(
        max_length=2,
        choices = UserType.choices,
        default=UserType.SHOPKEEPER
    )
    ratings = models.CharField(
        max_length=2,
        choices = Rating.choices,
        default=Rating.ZERO
    )
    username=models.CharField(max_length=50)
    pic_avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    objects=CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # @property delivery time of supplier


    def __str__(self):
        return self.username
