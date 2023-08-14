

# Удаление всех объектов модели Habit
from django.core.management import BaseCommand

from habit_tracker_app.models import Habit
from users.models import User



class Command(BaseCommand):
    help = 'Удаление тестовых данных из базы данных'

    def handle(self, *args, **kwargs):
        Habit.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно удалены!'))