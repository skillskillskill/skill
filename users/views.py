from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from posts.models import Post

from .forms import UserCreationForm, UserLoginForm, UserUpdateForm

# Create your views here.
User = get_user_model()


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 10


# 회원 가입 처리 뷰
class SignUpView(View):
    # GET 요청 처리 : 회원 가입 폼을 표시
    def get(self, request):
        # UserCreationForm 인스턴스 생성
        form = UserCreationForm()
        context = {"form": form}
        # signup.html 템플릿에 폼을 전달하여 렌더링
        return render(request, "signup.html", context)

    def post(self, request):
        # POST 데이터로 UserCreationForm 인스턴스 생성
        form = UserCreationForm(request.POST)
        # 폼 데이터가 유효한지 검증
        if form.is_valid():
            # 유효하다면 사용자 생성 및 저장
            user = form.save()
            # 생성된 사용자 생성 및 저장
            login(request, user)
            # 홈페이지로 리다이렉트
            return redirect("home")
        context = {"form": form}
        # 폼이 유효하지 않으면 에러와 함께 폼을 다시 표시
        return render(request, "login.html", context)


# Django의 기본 LoginView를 상속받아 커스텀 로그인 뷰 생성
class UserLoginView(View):
    # 사용할 로그인 템플릿 저장
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # 로그인 후 리디렉션할 URL 이름
            else:
                form.add_error(None, "사용자명 또는 비밀번호가 올바르지 않습니다.")

        return render(request, "login.html", {"form": form})


# 로그아웃 처리 함수
def user_logout(request):
    # 현재 사용자를 로그아웃
    logout(request)
    # 홈페이지로 리다이렉트
    return redirect("home")


# 사용자 프로필을 조회하는 뷰
class UserProfileView(View):
    def get(self, request, user_name):
        # 주어진 user_name 으로 사용자 객체 조회
        user = User.objects.get(user_name=User.user_name)
        context = {"user": user}
        # project.html 템플릿에 사용자 정보를 전달하여 렌더링
        return render(request, context)


# 사용자 정보 수정하는 뷰
class UserUpdateView(View):
    # GET 요청 처리 : 정보 수정 폼을 표시
    def get(self, request):
        # 현재 로그인한 사용자 정보로 UserUpdateForm 인스턴스 생성
        form = UserUpdateForm(instance=request.user)
        context = {"form": form}
        # update.html 템플릿에 폼을 전달하여 렌더링
        return render(request, context)

    # POST 요청 처리: 수정된 정보를 처리
    def post(self, request):
        # POST 데이터와 현재 사용자 인스턴스로 UserUpdateForm 생성
        form = UserUpdateForm(request.POST, instance=request.user)
        context = {"form": form}
        # 폼 데이터가 유효한지 검증
        if form.is_valid():
            # 유효하다면 변경사항 저장
            form.save()
            # 수정된 프로필 페이지로 리다이렉트
            return redirect("user_profile", user_name=request.user.user_name)

        # 폼이 유효하지 않으면 에러와 함께 폼을 다시 표시
        return render(request, context)
