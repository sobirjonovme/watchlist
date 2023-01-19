from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password', 'password2')


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        # To check passwords matching
        if data['password'] != data['password2']:
            raise ValidationError({'error': 'Passwords should be the same!'})
        print(data)
        # to check if a user does not already exist with this email
        email = data.get('email')
        if email and CustomUser.objects.filter(email=email).exists():
            raise ValidationError({'email': 'The user already registered with this email!'})

        return data
