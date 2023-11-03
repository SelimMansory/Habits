from django.contrib.auth.models import AbstractUser
from django.db import models
from telegram.models import Telegram

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """
    Пользователь
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=11, **NULLABLE, verbose_name='телефон')

    telegram = models.ForeignKey(Telegram, on_delete=models.SET_NULL, **NULLABLE, verbose_name='чат id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []