from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from likes.models import Like
from posts.models import Post

# Create your views here.


# 로그인 한 사용자만 이 뷰에 접근할 수 있도록 합니다.
@login_required
# POST 요청만을 허용합니다.
@require_POST
def toggle_like(request, post_id):
    """
    게시물에 대한 좋아요를 토글(추가/제거) 하는 뷰 함수
    """
    # 주어진 post_id 로 게시물을 조회하거나 404 에러를 반환합니다.
    post = get_object_or_404(Post, pk=post_id)

    # 현재 사용자와 게시물에 대한 좋아요 객체를 가져오거나 생성합니다.
    like, created = Like.objects.get_or_create(post_id=post, author_id=request.user)

    if not created:
        # 이미 좋아요가 존재하면 삭제합니다.
        like.delete()
        liked = False

    else:
        # 새로 생성된 경우 liked를 True로 설정합니다.
        liked = True

    return JsonResponse({"liked": liked, "like_count": post.like_set.count()})


@login_required
def like_list(request):
    """
    현재 사용자가 좋아요 한 게시물 목록을 보여주는 뷰 함수
    """

    # 현재 사용자가 좋아요한 게시물들을 조회합니다.
    liked_posts = Post.objects.filter(like__author_id=request.user)

    # 조회된 게시물들을 컨텍스트에 담아 템플릿에 전달합니다.
    context = {"liked_posts": liked_posts}

    # likes/like_list.html 템플릿을 렌더링하여 HTTP 응답을 반환합니다.
    return render(request, "likes/like_list_html", context)
