from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.throttling import AnonRateThrottle
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from films.models import StreamPlatform, Film, Review
from films.api.serializers import (
    StreamPlatformSerializer,
    StreamPlatformDetailSerializer,
    FilmSerializer,
    FilmDetailSerializer,
    ReviewSerializer,
)
from films.api.permissions import IsOwnerOrIsAdminOrReadOnly, IsAdminOrReadOnly
from films.api.throttling import GetUserRateThrottle, PostReviewThrottle
from films.api.pagination import FilmPagination


# =============   STREAM PLATFORM API VIEWs   ========================
class StreamPlatformListAPIView(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, GetUserRateThrottle]


class StreamPlatformDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformDetailSerializer

    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, GetUserRateThrottle]


# =============   FILM API VIEWs   ========================
class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all().order_by('-id')
    serializer_class = FilmSerializer

    pagination_class = FilmPagination
    permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle, GetUserRateThrottle]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'avg_rating', 'created_at']
    search_fields = ['title', ]
    filterset_fields = {
        'active': ['exact'],
        'platform__name': ['exact'],
        'avg_rating': ['lte', 'gte'],
    }


class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer

    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, GetUserRateThrottle]


# =============   REVIEW API VIEWs   ========================
class ReviewListAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, GetUserRateThrottle, PostReviewThrottle]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at']
    search_fields = ['review_author__username', 'review_text']

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(film__id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        film = Film.objects.get(pk=pk)

        review_user = self.request.user
        # if Review.objects.filter(film=film, review_author=review_user).exists():
        #     raise ValidationError({
        #         'error': 'You already left a review. One user can write only one review'
        #     })

        serializer.save(film=film, review_author=review_user)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsOwnerOrIsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, GetUserRateThrottle]
