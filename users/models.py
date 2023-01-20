from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


# Create your models here.
class CustomUser(AbstractUser):

    def get_tokens(self):
        token = Token.objects.get_or_create(user=self)
        data = {
            'token': token
        }

        return token
