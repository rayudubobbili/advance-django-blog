from django.contrib import admin
from .models import Post, Comments, Likes, Views, Tags


admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Views)
admin.site.register(Tags)
