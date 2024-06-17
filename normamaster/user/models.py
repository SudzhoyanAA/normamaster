from django.contrib.auth.models import AbstractUser
from django.db import models

from normamaster.constants import (
    MAX_NAME_LENGTH,
    MAX_EMAIL_LENGHT,
    MAX_FIELD_LENGTH
)
from .validatoins import username_validator


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тег',
        max_length=MAX_FIELD_LENGTH,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=MAX_FIELD_LENGTH,
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    REQUIRED_FIELDS = ('username', 'password')
    USERNAME_FIELD = ('email')

    USER_TYPES = (
        ('client', 'Клиент'),
        ('specialist', 'Специалист'),
    )
    user_type = models.CharField(
        verbose_name='Тип пользователя',
        choices=USER_TYPES,
        default='client',
        max_length=20,
    )

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=MAX_NAME_LENGTH,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=MAX_EMAIL_LENGHT,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=MAX_NAME_LENGTH
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=MAX_NAME_LENGTH
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='specialists',
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
