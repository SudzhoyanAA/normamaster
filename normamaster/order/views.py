from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import filters

from .models import Order
from user.models import Tag
from .serializers import TagSerializer, OrderGetSerializer, OrderSerializer
from user.validatoins import IsAdminAuthorOrReadOnly


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Тэг."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']


class OrderViewSet(viewsets.ModelViewSet):
    """Заказ."""
    queryset = Order.objects.all()
    # permission_classes = (IsAdminAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return OrderGetSerializer
        return OrderSerializer
