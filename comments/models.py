from django.db import models

from categories.models import Category
from posts.models import Post
from users.models import User

# Create your models here.


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Comment {self.comment_id} by {self.author_id.user_name}"
