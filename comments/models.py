from django.db import models

from categories.models import Category
from posts.models import Post
from users.models import User

# Create your models here.


class Comment(models.Model):
    # 댓글의 고유 식별자, 자동 증가
    comment_id = models.BigAutoField(primary_key=True)
    # 댓글 내용
    content = models.TextField()
    # 댓글 생성 시간, 자동 설정
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    # 연관된 게시물, 게시물 삭제 시 댓글도 삭제
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 댓글 작성자, 사용자 삭제 시 댓글도 삭제
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # 연관된 카테고리, 카테고리 삭제 시 댓글도 삭제
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 댓글 삭제 여부 표시
    is_delete = models.BooleanField(default=False)
    # 대댓글 구현을 위한 자기 참조, 선택적
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    # 객체의 문자열 표현
    def __str__(self):
        return f"Comment {self.comment_id} by {self.author_id.user_name}"
