from django.db import models
from django.utils import timezone
from twitteruser.models import CustomUserModel

# Got help from Howard Post on this part at study hall, 9/5/2020
# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=140)
    date_tweeted = models.DateTimeField(default=timezone.now)
    user_tweeted = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.text