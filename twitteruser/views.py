from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your views here.
@login_required
def homepage_view(request):
    user_info = TwitterUser.objects.get(id=request.user.id)
    users_following = user_info.followed_users.all().count()
    tweets = Tweet.objects.all().order_by('-date_tweeted')
    tweet_count = Tweet.objects.filter(user_tweeted=request.user).count()
    return render(request, 'homepage.html', {
        'user_info': user_info,
        'users_following': users_following,
        'tweets': tweets,
        'tweet_count': tweet_count
    })

def profilepage_view(request, user_id):
    profile_user = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user_tweeted=profile_user).order_by('-date_tweeted')
    return render(request, 'profilepage.html', {
        'profile_user': profile_user,
        'tweets': tweets
    })

def tweetpage_view(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, 'tweetpage.html', {
        'tweet': tweet
    })

def follow_view(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    request.user.followed_users.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unfollow_view(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    request.user.followed_users.remove(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))