from django.urls import path
from .views import UserLoginAPIView, UserRegisterAPIView, UserLogoutAPIView

urlpatterns = [
    path('api/login/', UserLoginAPIView.as_view(), name='api_login'),
    path('api/register/', UserRegisterAPIView.as_view(), name='api_register'),
    path('api/logout/', UserLogoutAPIView.as_view(), name='api_logout'),
]