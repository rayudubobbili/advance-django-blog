from django.urls import path
from .views import homepage, post_listview, Post_detailview

app_name = 'blog'
urlpatterns = [
    path('', homepage, name="homeview"),
    path('posts', post_listview, name="listview"),
    path('<slug:slug>', Post_detailview.as_view(), name="detailview"),
]
