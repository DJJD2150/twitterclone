from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser

# Got help from Detrich Schilling in study hall.
# Create your models here.
class Notification(models.Model):
    is_seen = models.BooleanField(default=False)
    notification_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    notification_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.notification_tweet.text