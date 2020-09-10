from django.shortcuts import render, redirect, HttpResponseRedirect

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification

import re

# Create your views here.
def create_tweet_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(text = data.get('text'),
                                 user_tweeted = request.user)
            notification = re.findall(r"@([\w]+)", data.get('text'))
            if notification:
                for username in notification:
                    user = TwitterUser.objects.get(username=username)
                    Notification.objects.create(notification_tweet = tweet,
                                                notification_user = user,
                                                )
            return redirect('/')
    form = TweetForm()
    return render(request, 'tweet_form.html', {"form": form})
