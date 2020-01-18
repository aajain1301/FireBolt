from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# from multiselectfield import MultiSelectField

# Create your models here.
class Crop(models.Model):
    crop = models.CharField(max_length=20)


class User(AbstractUser):
    user_type   = models.BooleanField(default=False)

    # If user_type is Seller
    crops       = models.ManyToManyField(Crop)
    warehouse   = models.BooleanField(default=False)
    transport   = models.BooleanField(default=False)
