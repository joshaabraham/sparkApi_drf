from django.urls import path
from . import views

urlpatterns = [
    path("albums/", views.AlbumListCreateView.as_view(), name="album_list_create"),
    path("albums/<int:pk>/", views.AlbumRetrieveUpdateDestroyView.as_view(), name="album_detail"),
    path("images/", views.ImageListCreateView.as_view(), name="image_list_create"),
    path("images/<int:pk>/", views.ImageRetrieveUpdateDestroyView.as_view(), name="image_detail"),
]