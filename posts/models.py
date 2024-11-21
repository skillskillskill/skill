from django.db import models

from users.models import User

# Create your models here.


class Post(models.Model):
    # 게시글 고유 식별자
    post_id = models.BigAutoField(primary_key=True)
    # 게시물 컨텐츠
    content = models.TextField()
    # 게시물 URL 슬러그
    slug = models.SlugField(max_length=100, unique=True)
    # 게시물 조회수
    view_count = models.IntegerField(default=0)
    # 게시물 작성 날짜 및 시간
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    # 게시물 수정 날짜 및 시간
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    # 게시물 작성자와의 관계
    # 작성자 계정이 삭제되면 해당 게시물도 함께 삭제
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug

    def get_like_count(self):
        """이 게시물 좋아요 수를 반환합니다"""
        return self.like_set.count()

    def is_liked_by(self, user):
        """주어진 사용자가 이 게시물을 좋아요 했는지 확인합니다"""
        return self.like_set.filter(author_id=user).exists()
