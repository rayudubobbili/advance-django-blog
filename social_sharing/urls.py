from django.urls import path
from . import views


app_name = "social_sharing"
urlpatterns = [
    path('facebook/', views.facebook, name='facebook_share'),
    path('google_plus/', views.google_plus, name='google_plus_share'),
    path('twitter', views.twitter, name='twitter_share'),
    path('reddit', views.reddit, name='reddit_share'),
]
