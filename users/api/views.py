from rest_framework.generics import CreateAPIView

from .serializers import RegistrationSerializer
from users.models import CustomUser


class RegistrationAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
