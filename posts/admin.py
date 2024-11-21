from django.contrib import admin

from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content",
        "view_count",
        "created_at",
        "updated_at",
    ]
    list_filter = ["author_id__post", "created_at", "updated_at"]
