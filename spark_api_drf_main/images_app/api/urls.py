from django.urls import path
from . import views

urlpatterns = [
    path("albumsCreateList/", views.AlbumListCreateView.as_view(), name="album_list_create"),
    path("album/<int:pk>/", views.AlbumRetrieveUpdateDestroyView.as_view(), name="album_detail"),
    path("imagesCreateList/", views.ImageListCreateView.as_view(), name="image_list_create"),
    path("image/<int:pk>/", views.ImageRetrieveUpdateDestroyView.as_view(), name="image_detail"),
]