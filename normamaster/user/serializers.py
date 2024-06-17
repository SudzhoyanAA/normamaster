from djoser.serializers import UserCreateSerializer, UserSerializer

from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Tag

User = get_user_model()


class UserGetSerializer(UserSerializer):
    """Получение информации о пользователе."""

    orders = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'user_type',
            'orders',
        )

    def get_orders(self, obj):
        from order.serializers import OrderShortSerializer
        orders = obj.orders.all()
        return OrderShortSerializer(orders, many=True).data


class UserSignUpSerializer(UserCreateSerializer):
    """Создание пользователя."""

    user_type = serializers.ChoiceField(
        choices=User.USER_TYPES, default='client'
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, required=False
    )

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'user_type',
            'tags',
        )

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user.tags.set(tags_data)
        return user

    def validate(self, attrs):
        tags_data = attrs.pop('tags', [])
        return attrs
