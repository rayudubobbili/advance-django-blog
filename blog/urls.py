from django.urls import path
from .views import homepage, post_listview, Post_detailview, category_listview, category_detailView, tag_listview, tag_detailview, contact_view

app_name = 'blog'
urlpatterns = [
    path('', homepage, name="homeview"),
    path('posts', post_listview, name="listview"),
    path('<slug:slug>', Post_detailview.as_view(), name="detailview"),
    path('categories/', category_listview, name="category-listview"),
    path('categories/<slug:category>', category_detailView, name="category-detailview"),
    path('tags/', tag_listview, name="tag-listview"),
    path('tags/<slug:tag>/', tag_detailview, name="tag-detailview"),
    path('contactus/', contact_view, name="contact-view"),
]
