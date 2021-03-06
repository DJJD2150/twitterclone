"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from twitteruser import views as user_view
from tweet import views as tweet_view
from authentication import views as auth_view
from notification import views as note_view

urlpatterns = [
    path('', user_view.HomepageView.as_view(), name="homepage"),
    path('profilepage/<int:user_id>/', user_view.ProfilePageView.as_view(), name="profilepage"),
    path('tweetpage/<int:tweet_id>/', user_view.TweetPageView.as_view(), name="tweetpage"),
    path('notifications/', note_view.notification_view, name="notifications"),
    path('follow/<int:user_id>/', user_view.follow_view, name="follow"),
    path('unfollow/<int:user_id>/', user_view.unfollow_view, name="unfollow"),
    path('tweet/', tweet_view.CreateTweetFormView.as_view(), name="tweet"),
    path('login/', auth_view.login_view, name="login"),
    path('signup/', auth_view.signup_view, name="signup"),
    path('logout/', auth_view.logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
