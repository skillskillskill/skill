from django.db import models

from posts.models import Post
from users.models import User

# Create your models here.


class Like(models.Model):
    like_id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post_id", "author_id")

    def __str__(self):
        return f"Like by {self.author_id.user_name} on {self.post_id.slug}"
