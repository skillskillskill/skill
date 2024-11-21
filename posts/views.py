from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from posts.models import Post

# Create your views here.


class PostListView(ListView):
    # Post 모델의 목록을 표시하는 뷰
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class PostDetailView(DetailView):
    # 개별 Post의 상세 정보를 표시하는 뷰
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


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


class PostDeleteView(LoginRequiredMixin, DeleteView):
    # Post 를 삭제하는 뷰, 로그인 필요
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    object: Any = None
