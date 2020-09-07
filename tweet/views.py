from django.shortcuts import render, redirect, HttpResponseRedirect

from tweet.forms import TweetForm
from tweet.models import Tweet

# Create your views here.
def create_tweet_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(text = data.get('text'),
                                 user_tweeted = request.user)
            return redirect('/') 
    form = TweetForm()
    return render(request, 'tweet_form.html', {"form": form})
