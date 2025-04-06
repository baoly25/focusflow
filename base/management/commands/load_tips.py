from django.core.management.base import BaseCommand
from base.models import StressTip

class Command(BaseCommand):
    help = 'Load predefined stress tips into the database'

    def handle(self, *args, **kwargs):
        tips = [
            ("Box Breathing", "Inhale for 4 seconds, hold for 4, exhale for 4, hold again for 4. Repeat."),
            ("Quick Walk", "Take a 5-10 minute walk to reset your body and clear your mind."),
            ("Write It Out", "Dump your thoughts in a journal or note app. Get it out of your head."),
            ("Stretch Break", "Stand up and stretch your arms, back, and neck for a few minutes."),
            ("Hydrate", "Drink water. Dehydration can affect your mood and focus."),
            ("Do One Thing", "Pick one small task and complete it. Avoid overloading yourself."),
            ("Screen Pause", "Close your eyes or look away from screens for 20 seconds."),
            ("Deep Breathing", "Slowly inhale through your nose and exhale through your mouth."),
            ("Progressive Relaxation", "Tense and relax each muscle group starting from your feet."),
            ("Gratitude Pause", "List 3 things you're grateful for. It shifts focus away from stress.")
        ]

        for title, content in tips:
            StressTip.objects.get_or_create(title=title, content=content)

        self.stdout.write(self.style.SUCCESS('Loaded stress tips.'))
