from celery import shared_task
from config import settings
from users.models import User
from .models import Habit
import telebot


from datetime import datetime

@shared_task
def check_habits_and_notify():
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_API)
    habits = Habit.objects.all()
    current_time = datetime.now().time()
    for habit in habits:
        if habit.time == current_time:
            chat_id = habit.owner.chat_id
            message = f"Пора выполнить привычку: {habit.name}!\nМесто: {habit.place}"

            bot.send_message(chat_id, message)
