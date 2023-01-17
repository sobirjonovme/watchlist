from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from .models import Review


@receiver(pre_save, sender=Review)
def review_create(sender, instance, **kwargs):
    if instance.id is None:
        film = instance.film
        avg_rating = (film.avg_rating*film.number_rating + instance.rating) / (film.number_rating+1)
        # film.avg_rating = round(avg_rating, 1)
        film.avg_rating = avg_rating
        film.number_rating += 1
        film.save()
    else:
        film = instance.film
        old_rating = Review.objects.get(id=instance.id).rating
        avg_rating = (film.avg_rating*film.number_rating - old_rating + instance.rating) / film.number_rating
        # film.avg_rating = round(avg_rating, 1)
        film.avg_rating = avg_rating
        film.save()


@receiver(pre_delete, sender=Review)
def review_delete(sender, instance, **kwargs):
    film = instance.film
    film.avg_rating = (film.avg_rating*film.number_rating - instance.rating) / (film.number_rating-1)
    film.number_rating -= 1
    film.save()
