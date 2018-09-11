from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homepage, name="homeview"),
    path('posts', views.post_listview, name="listview"),
    path('<slug:slug>', views.post_detailview, name="detailview"),
    path('categories/', views.category_listview, name="category-listview"),
    path('categories/<slug:category>', views.category_detailView, name="category-detailview"),
    path('tags/', views.tag_listview, name="tag-listview"),
    path('tags/<slug:tag>/', views.tag_detailview, name="tag-detailview"),
    path('contactus/', views.contact_view, name="contact-view"),
]
