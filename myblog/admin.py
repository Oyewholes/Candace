from django.contrib import admin
from myblog.models import Post, Category, Comment, Subscriber
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Subscriber)