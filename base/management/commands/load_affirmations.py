from django.core.management.base import BaseCommand
from base.models import Affirmation

class Command(BaseCommand):
    help = 'Load sample affirmations into the database'

    def handle(self, *args, **kwargs):
        affirmations = [
            {"title": "You Are Capable", "content": "You have everything you need to overcome today's challenges."},
            {"title": "You Matter", "content": "Your thoughts, feelings, and presence have value."},
            {"title": "Keep Going", "content": "Progress takes time, don't stop now."},
            {"title": "You Deserve Rest", "content": "Resting is productive too. Your body and mind need it."},
            {"title": "You Can Handle This", "content": "No matter how hard it gets, you have handled worse before."},
            {"title": "Progress Is Personal", "content": "Your pace is valid. You don't need to match anyone else's timeline."},
            {"title": "You're Learning", "content": "Mistakes aren't failure, they're part of the process."},
            {"title": "You're Allowed to Say No", "content": "Protecting your time and energy is a form of self-respect."},
            {"title": "Calm Is Possible", "content": "Take a deep breath. You can approach this with clarity."},
            {"title": "You've Got Through Before", "content": "You've faced hard days and made it. This one is no different."}
        ]

        for affirm in affirmations:
            Affirmation.objects.get_or_create(title=affirm["title"], content=affirm["content"])

        self.stdout.write(self.style.SUCCESS('Affirmations loaded successfully.'))
