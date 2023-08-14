from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='admin@gmail.com',
            first_name='Admin',
            last_name='Gmail',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('qwerty')
        user.save()
