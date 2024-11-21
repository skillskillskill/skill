from django.db import models

# Create your models here.


class Category(models.Model):
    # 카테고리 고유 식별자
    category_id = models.BigAutoField(primary_key=True)
    # 카테고리 이름
    category_name = models.CharField(max_length=50)
    # URL 친화적인 문자열
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name
