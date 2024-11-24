from django.urls import path

from .views import ItemCreateListView, ItemDetailUpdateDeleteView

urlpatterns = [
    path("items/", ItemCreateListView.as_view()),
    path("items/<str:id>", ItemDetailUpdateDeleteView.as_view()),
]
