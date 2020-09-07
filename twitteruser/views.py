from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitteruser.models import CustomUserModel
from tweet.models import Tweet

# Create your views here.
@login_required
def homepage_view(request):
    user_info = CustomUserModel.objects.get(id=request.user.id)
    users_following = user_info.followed_users.all().count()
    tweets = Tweet.objects.all().order_by('-date_tweeted')
    return render(request, 'homepage.html', {
        'user_info': user_info,
        'users_following': users_following,
        'tweets': tweets
    })

def profilepage_view(request, user_id):
    username = CustomUserModel.objects.get(id=user_id)
    tweets = Tweet.objects.filter(user_tweeted=username).order_by('-date_tweeted')
    return render(request, 'profilepage.html', {
        'username': username,
        'tweets': tweets
    })