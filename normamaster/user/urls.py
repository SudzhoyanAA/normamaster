from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, CustomTokenObtainPairView

router = DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]
