from django.urls import path

from .views import (
    RoleCreateListView,
    RoleDetailUpdateDeleteView,
    UserCreateListView,
    UserDetailUpdateDeleteView,
)

urlpatterns = [
    path("roles/", RoleCreateListView.as_view()),
    path("roles/<str:id>", RoleDetailUpdateDeleteView.as_view()),
    path("users/", UserCreateListView.as_view()),
    path("users/<str:id>", UserDetailUpdateDeleteView.as_view()),
]
