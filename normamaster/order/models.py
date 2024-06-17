from django.contrib.auth import get_user_model

from django.db import models

from user.models import Tag


User = get_user_model()


class Order(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Автор'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        related_name='orders'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-id']

    def __str__(self):
        return f"Заказ {self.id} от {self.author.username}"
