from django.urls import path

from likes import views

app_name = "likes"


urlpatterns = [
    path("toggle/<int:post_id>/", views.toggle_like, name="toggle"),
    path("list/", views.like_list, name="list"),
]
