from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/<str:user_name>/", views.UserProfileView.as_view(), name="profile"),
    path("update/", views.UserUpdateView.as_view(), name="update"),
]
