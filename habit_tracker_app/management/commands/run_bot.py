import telebot
from django.core.management import BaseCommand
from config import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TELEGRAM_BOT_API)

        @bot.message_handler(commands=['get_chat_id'])
        def get_chat_id(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, f"Ваш chat_id: {chat_id}")

        bot.polling()
