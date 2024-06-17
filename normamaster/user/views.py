from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from djoser.views import UserViewSet

from .serializers import UserSignUpSerializer
from .validatoins import IsAdminAuthorOrReadOnly
from .authentication import CustomTokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomUserViewSet(UserViewSet):
    """Костомный пользователь."""
    permission_classes = (IsAdminAuthorOrReadOnly,)

    def get_permissions(self):
        if self.action == 'me':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSignUpSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        user_type = self.request.data.get('user_type', 'client')
        serializer.save(user_type=user_type)

        if user_type == 'specialist':
            tags_data = self.request.data.get('tags', [])
            user = serializer.instance
            user.tags.set(tags_data)
