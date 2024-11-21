from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from posts.models import Post

# Create your views here.


class PostListView(ListView):
    # Post 모델의 목록을 표시하는 뷰
    # 사용할 모델 지정
    model = Post
    # 사용할 템플릿 파일 지정
    template_name = "posts/post_list.html"
    # 템플릿에서 사용할 객체 리스트의 이름
    context_object_name = "posts"
    # 생성일 기준 내림차순 정렬
    ordering = ["-created_at"]
    # 한 페이지당 표시할 게시물 수
    paginate_by = 10

    def get_queryset(self):
        # 기본 쿼리셋 가져오기
        queryset = super().get_queryset()
        # URL 파라미터에서 카테고리와 검색어 가져오기
        category = self.request.GET.get("category")
        search = self.request.GET.get("search")

        # 카테고리가 지정된 경우 필터링
        if category:
            queryset = queryset.filter(category__slug=category)

        # 검색어가 있는 경우 제목과 내용에서 검색
        if search:
            queryset = queryset.filter(
                Q(title__incontains=search) | Q(content__icontains=search)
            )


class PostDetailView(DetailView):
    # 개별 Post의 상세 정보를 표시하는 뷰
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_object(self):
        # 기본 객체 가져오기
        obj = super().get_object()
        # 조회수 증가
        obj.view_count += 1
        obj.save()
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):
    # 새 Post를 생성하는 뷰, 로그인 필요
    model = Post
    template_name = "posts/post_form.html"
    fields = ["content", "slug"]
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        # 폼 유혀성 검사 후 작성자 지정
        form.instance.author_id = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # 기존 Post를 수정하는 뷰, 로그인 필요
    model = Post
    template_name = "posts/post_form.html"
    fields = ["content", "slug"]
    success_url = reverse_lazy("post_list")

    def test_func(self):
        # 현재 사용자가 게시물 작성자인지 확인
        return self.get_object().author_id == self.request.user


class PostDeleteView(LoginRequiredMixin, DeleteView):
    # Post 를 삭제하는 뷰, 로그인 필요
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    object: Any = None

    def test_func(self):
        # 현재 사용자가 게시물 작성자인지 확인
        return self.get_object().author_id == self.request.user
