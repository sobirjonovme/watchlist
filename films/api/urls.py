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

    path('platforms/list/', StreamPlatformListAPIView.as_view(), name='platform-list'),
    path('platforms/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='platform-detail'),

    path('<int:pk>/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
