from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView 
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="sign-up"),
    path('login/', TokenObtainPairView.as_view(), name="token-obtain"),
    path('login/refresh/', TokenRefreshView.as_view(), name="token-refresh")
]