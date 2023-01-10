from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import CustomUser


# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField()

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=60)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(
        StreamPlatform,
        on_delete=models.CASCADE,
        related_name='platform_films'
    )
    # avg_rating = models.FloatField(default=0)
    # number_rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_reviews'
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.CharField(max_length=250)
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='film_reviews'
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} | {self.film.title} | {self.review_author}"
