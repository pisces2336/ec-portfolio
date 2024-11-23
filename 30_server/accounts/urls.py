from django.urls import path

from .views import RoleCreateListView, RoleDetailUpdateDeleteView

urlpatterns = [
    path("roles/", RoleCreateListView.as_view()),
    path("roles/<str:id>", RoleDetailUpdateDeleteView.as_view()),
]
