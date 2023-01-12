from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from films.models import StreamPlatform, Film, Review

from .serializers import (
    StreamPlatformSerializer,
    StreamPlatformDetailSerializer,
    FilmSerializer,
    FilmDetailSerializer,
    ReviewSerializer,
)


# =============   STREAM PLATFORM API VIEWs   ========================
class StreamPlatformListAPIView(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class StreamPlatformDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformDetailSerializer


# =============   FILM API VIEWs   ========================
class FilmListAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer


# =============   REVIEW API VIEWs   ========================
class ReviewListAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(film__id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        film = Film.objects.get(pk=pk)

        review_user = self.request.user

        serializer.save(film=film, review_author=review_user)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
