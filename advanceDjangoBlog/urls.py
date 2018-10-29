from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('<slug:slug>/share/', include('social_sharing.urls')),
    path('subscribe/', include('subscribe.urls')),
]
