from django.contrib import admin
from .models import Picture,Profile,Comment,Follow, Unfollow, Likes
admin.site.register(Picture)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Unfollow)
admin.site.register(Likes)

# Register your models here.

