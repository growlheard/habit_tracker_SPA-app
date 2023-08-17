from config import settings
from django.core.management.base import BaseCommand
import telebot
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TELEGRAM_BOT_API)

        @bot.message_handler(commands=['get_chat_id'])
        def get_chat_id(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, f"Ваш chat_id: {chat_id}")

        @bot.message_handler(func=lambda message: True)
        def greet_new_user(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, "Привет! Я бот. Чтобы узнать свой chat_id, введите команду /get_chat_id.")

        bot.polling()
