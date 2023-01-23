from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # For Token Authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # For JWT Authentication

from users.api.views import RegistrationAPIView, LogOutAPIView

app_name = 'users'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('logout/', LogOutAPIView.as_view(), name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
