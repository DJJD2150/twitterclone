from django.db import models
from django.contrib.auth.models import AbstractUser

# Got help from Howard Post on this part at study hall, 9/5/2020
# Create your models here.
class CustomUserModel(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    followed_users = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return "@" + self.username
