from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token  # For Token Authentication
from rest_framework_simplejwt.tokens import RefreshToken  # For JWT Authentication


# Create your models here.
class CustomUser(AbstractUser):

    def get_tokens(self):
        # # ===============   For Token Authentication   ============
        # token, created = Token.objects.get_or_create(user=self)
        # # token = Token.objects.get(user=self)
        # data = {
        #     'token': token.key,
        # }

        # ===============   For JWT Authentication   ============
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data
