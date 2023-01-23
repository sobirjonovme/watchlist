from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError

from films.models import StreamPlatform, Film, Review
from .serializers import (
    StreamPlatformSerializer,
    StreamPlatformDetailSerializer,
    FilmSerializer,
    FilmDetailSerializer,
    ReviewSerializer,
)
from .permissions import IsOwnerOrIsAdminOrReadOnly, IsAdminOrReadOnly


# =============   STREAM PLATFORM API VIEWs   ========================
class StreamPlatformListAPIView(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    permission_classes = [IsAdminOrReadOnly]


class StreamPlatformDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformDetailSerializer

    permission_classes = [IsAdminOrReadOnly]


# =============   FILM API VIEWs   ========================
class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    permission_classes = [IsAdminOrReadOnly]


class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer

    permission_classes = [IsAdminOrReadOnly]


# =============   REVIEW API VIEWs   ========================
class ReviewListAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(film__id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        film = Film.objects.get(pk=pk)

        review_user = self.request.user
        if Review.objects.filter(film=film, review_author=review_user).exists():
            raise ValidationError({
                'error': 'You already left a review. One user can write only one review'
            })

        serializer.save(film=film, review_author=review_user)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsOwnerOrIsAdminOrReadOnly]
