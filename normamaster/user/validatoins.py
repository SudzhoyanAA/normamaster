import re

from django.core.exceptions import ValidationError
from rest_framework import permissions

from normamaster.constants import USER_ME


def username_validator(value):
    regex = r'^[\w.@+-]+\Z'
    if re.search(regex, value) is None:
        invalid_characters = set(re.findall(r'[^\w.@+-]', value))
        raise ValidationError(
            (
                f'Недопустимые символы {invalid_characters} в username. '
                f'username может содержать только буквы, цифры и '
                f'знаки @/./+/-/_.'
            ),
        )

    if value.lower() == USER_ME:
        raise ValidationError(
            f'Использовать имя <{USER_ME}> в качестве '
            f'username запрещено.'
        )


class IsAdminAuthorOrReadOnly(permissions.BasePermission):
    """Доступ автору и администратору"""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_staff
            or request.user.is_superuser
        )
