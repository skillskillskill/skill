from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), user_name=user_name, nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password, nickname):
        user = self.create_user(
            email=email,
            password=password,
            user_name=user_name,
            nickname=nickname,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# django 기본 abstractuser 를 상속받아 확장한다.
class User(AbstractBaseUser, PermissionsMixin):
    # 사용자 고유 식별자 ID
    user_id = models.BigAutoField(primary_key=True)
    # 사용자의 고유한 사용자 명
    user_name = models.CharField(max_length=30, unique=True)
    # 사용자의 별명
    nickname = models.CharField(max_length=30, unique=True)
    # 사용자 이메일
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    # 사용자 비밀번호
    password = models.CharField(max_length=128)
    # 사용자 계정의 활성화 여부
    is_active = models.BooleanField(default=True)
    # 관리자 권한 여부
    is_staff = models.BooleanField(default=False)
    # 사용자 계정 정보 생성 날짜 및 시간
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    # 사용자 계정 정보 수정 날짜 및 시간
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # 사용자 인증에 사용될 필드
    USERNAME_FIELD = "email"
    # 사용자 생성 시 필수 입력 필드
    REQUIRED_FIELDS = ["user_name", "nickname", "password"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
