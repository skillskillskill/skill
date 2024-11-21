from django.urls import path

from posts import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    # path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    # path("new/", views.PostCreateView.as_view(), name="create"),
    # path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="update"),
    # path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    # path(
    #     "category/<slug:category_slug>/",
    #     views.PostListView.as_view(),
    #     name="category_list",
    # ),
    # path("search/", views.PostListView.as_view(), name="search"),
    # path("<slug:slug>/", views.PostDetailView.as_view(), name="detail_slug"),
]
