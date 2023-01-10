from django.contrib import admin

from .models import StreamPlatform, Film, Review

# Register your models here.
admin.site.register(StreamPlatform)
admin.site.register(Film)
admin.site.register(Review)
