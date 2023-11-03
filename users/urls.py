from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from users.views import UserCreateAPIView, UserAPIView, UserListAPIView


app_name = UsersConfig.name

urlpatterns = [
    #  users
    path('', UserListAPIView.as_view(), name='list_user'),
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('user/<int:pk>/', UserAPIView.as_view(), name='user'),

    #  token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]