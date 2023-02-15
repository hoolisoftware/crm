from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from typing import Tuple, Dict, Optional
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--email', help="Admin's email", required=True
        )

        parser.add_argument(
            '--password', help="Admin's password", required=True
        )

    def handle(self, *args: Tuple, **options: Dict) -> Optional[str]:
        if not User.objects.filter(email=options['email']).exists():
            User.objects.create_superuser(
                email=options['email'],
                password=options['password']
            )
