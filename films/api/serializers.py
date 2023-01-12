from rest_framework import serializers

from films.models import StreamPlatform, Film, Review
from users.api.serializers import CustomUserSerializer


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class StreamPlatformDetailSerializer(serializers.ModelSerializer):
    platform_films = FilmSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    review_author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('film', )


class FilmDetailSerializer(serializers.ModelSerializer):
    platform = StreamPlatformSerializer(read_only=True)
    film_reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Film
        fields = '__all__'


