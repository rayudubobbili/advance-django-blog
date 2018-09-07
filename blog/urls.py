from django.urls import path
from .views import homepage, Post_list_view, Post_detail_view

app_name = 'blog'
urlpatterns = [
    path('', homepage, name="homeview"),
    path('posts', Post_list_view.as_view(), name="listview"),
    path('<slug:slug>', Post_detail_view.as_view(), name="detailview"),
]
