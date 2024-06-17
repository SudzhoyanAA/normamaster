from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, TagViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]
