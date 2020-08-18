from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command create Facilites"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="It's Hi")

    def handle(self, *args, **options):
        facilites = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilites:
            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilites has been created"))
