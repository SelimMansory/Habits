import os
from datetime import datetime
import telebot
from celery import shared_task
from habits.models import Habit


@shared_task()
def send_message_tegram():
    telegram_token = os.getenv('TELEGRAM_BOT_API')
    bot = telebot.TeleBot(telegram_token)
    habits = Habit.objects.all()
    for habit in habits:
        if habit.time == datetime.now().time():
            telegram = habit.owner.telegram
            if telegram is not None:
                bot.send_message(telegram.chat_id, f'я буду {habit.action} в {habit.time} в {habit.place}')