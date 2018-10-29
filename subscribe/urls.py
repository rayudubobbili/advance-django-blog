from django.urls import path
from . import views


app_name = "subscriber"
urlpatterns = [
    path('', views.subscriber, name="subscribe_new"),
    path('new', views.subscriber, name="subscribe_new"),
    path('cancel', views.subscriber_cancel_form, name="subscribe_cancel_form"),
    path('cancel/<name>', views.subscriber_cancel, name="subscribe_cancel"),
    path('cancel/success', views.subscriber_cancel, name="subscribe_cancel"),
]
