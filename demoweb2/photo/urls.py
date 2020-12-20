from django.urls import path
from photo.views import AlbumLV, AlbumDV, PhotoDV, AlbumPhotoCV, AlbumChangeLV, AlbumPhotoUV, AlbumDelV, PhotoCV, PhotoChangeLV, PhotoUV, PhotoDelV

app_name='photo'
urlpatterns = [
    # Example: /photo/
    path('',AlbumLV.as_view(), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album', AlbumLV.as_view(), name='album_list'),

    # Example: /photo/album/99/
    path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'),

    # Example: /photo/photo/99/
    path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),

    # Example: /photo/album/add/
    path('album/add/', AlbumPhotoCV.as_view(), name="album_add",),

    # Example: /photo/album/change/
    path('album/change/', AlbumChangeLV.as_view(), name="album_change",),

    # Example: /photo/album/99/update/
    path('<int:pk>/update/', AlbumPhotoUV.as_view(), name="album_update",),

    # Example: /photo/album/99/delete/
    path('<int:pk>/delete/', AlbumDelV.as_view(), name="album_delete",),

    # Example: /photo/photo/add/
    path('album/add/', PhotoCV.as_view(), name="photo_add",),

    # Example: /photo/photo/change/
    path('album/change/', PhotoChangeLV.as_view(), name="photo_change",),

    # Example: /photo/photo/99/update/
    path('<int:pk>/update/', PhotoUV.as_view(), name="photo_update",),

    # Example: /photo/photo/99/delete/
    path('<int:pk>/delete/', PhotoDelV.as_view(), name="photo_delete",),
]