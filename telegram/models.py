from django.db import models


class Telegram(models.Model):
    """
    Телеграм
    """
    chat_id = models.CharField(max_length=100, verbose_name='чат id')
    is_active = models.BooleanField(default=False, verbose_name='статус')

    def __str__(self):
        return f'{self.chat_id}, {self.is_active}'

    class Meta:
        verbose_name = 'телеграм'
        verbose_name_plural = 'телеграмы'