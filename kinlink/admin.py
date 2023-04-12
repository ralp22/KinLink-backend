from django.contrib import admin
from .models import UserProfile, UserImageSelection, Relationship, Post, Comment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserImageSelection)
admin.site.register(Relationship)
admin.site.register(Post)
admin.site.register(Comment)
