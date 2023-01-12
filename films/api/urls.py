from django.urls import path

from .views import (
    StreamPlatformListAPIView,
    StreamPlatformDetailAPIView,

    FilmListAPIView,
    FilmDetailAPIView,

    ReviewListAPIView,
    ReviewDetailAPIView,
)


app_name = 'films'

urlpatterns = [
    path('list/', FilmListAPIView.as_view(), name='film-list'),
    path('<int:pk>/', FilmDetailAPIView.as_view(), name='film-detail'),

    path('platform/list/', StreamPlatformListAPIView.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='platform-detail'),

    path('<int:pk>/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
