from django.db import models
from config import settings


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """
    Привычка
    """
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    pleasant_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    binding_habit = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, verbose_name='связная привычка')
    period = models.PositiveIntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    execution_time = models.TimeField(verbose_name='время выполнения')
    is_publish = models.BooleanField(default=False, verbose_name='признак публичности')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'я буду {self.action} в {self.action} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'