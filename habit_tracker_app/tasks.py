from celery import shared_task
from config import settings
from .models import Habit
import telebot

from datetime import datetime

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API)


@shared_task
def check_habits_and_notify():
    habits = Habit.objects.all()
    current_time = datetime.now().time().strftime("%H:%M")

    for habit in habits:
        habit_time = habit.time.strftime("%H:%M")

        if habit_time == current_time:
            chat_id = habit.owner.chat_id
            message = f"Пора выполнить привычку: {habit.name}!\nМесто: {habit.place}"
            bot.send_message(chat_id, message)
            return print(f"Отправлено сообщение: {message}")





