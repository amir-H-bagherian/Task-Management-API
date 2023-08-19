from django.urls import path
from .views import CustomUserListCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView 
)


urlpatterns = [
    path('user/', CustomUserListCreateView.as_view(), name="list-create"),
    path('login/', TokenObtainPairView.as_view(), name="token-obtain"),
    path('login/refresh/', TokenRefreshView.as_view(), name="token-refresh")
]