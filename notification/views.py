from django.shortcuts import render
from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser

# Create your views here.
def notification_view(request):
    notifications = Notification.objects.filter(notification_user__username = request.user.username)
    not_seen_notifications = []
    for notification in notifications:
        if notification.is_seen == False:
            not_seen_notifications.append(notification.notification_tweet)
        notification.is_seen = True
        notification.save()
    return render(request, 'notifications.html', {
        'tweets': not_seen_notifications
    })