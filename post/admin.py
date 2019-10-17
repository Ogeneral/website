from post.models import Post
from post.models import Comment
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Your_name', 'Your_Post_title', 'Your_Post', 'id']}),
    ]


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'text', 'post',]})
   ]


admin.site.register(Comment, CommentAdmin)