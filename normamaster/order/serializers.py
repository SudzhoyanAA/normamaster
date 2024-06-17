from rest_framework import serializers

from order.models import Order
from user.models import Tag
from user.serializers import UserGetSerializer


class TagSerializer(serializers.ModelSerializer):
    """Тэг."""

    class Meta:
        model = Tag
        fields = '__all__'


class OrderGetSerializer(serializers.ModelSerializer):
    """Получение информации о заказе."""

    tags = TagSerializer(
        many=True,
        read_only=True,
    )
    author = UserGetSerializer(
        read_only=True,
    )

    class Meta:
        model = Order
        fields = '__all__'


class OrderShortSerializer(serializers.ModelSerializer):
    """Краткая информация о заказе."""

    class Meta:
        model = Order
        fields = (
            'id',
            'author',
            'tags',
            'cost',
        )


class OrderSerializer(serializers.ModelSerializer):
    """Создание заказа."""

    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'author',
            'address',
            'date',
            'cost',
            'tags',
            'description'
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        order = Order.objects.create(**validated_data)
        order.tags.set(tags_data)
        return order
