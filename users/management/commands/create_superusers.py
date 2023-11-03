from django.core.management import BaseCommand
from users.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('SUPER_USER_EMAIL'),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('SUPER_USER_PASSWORD'))
        user.save()