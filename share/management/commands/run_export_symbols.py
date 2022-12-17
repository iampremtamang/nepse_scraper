import json
from django.core.management.base import BaseCommand, CommandError

from share.models import Security


class Command(BaseCommand):
    help = 'Export security symbols'
    
    def handle(self, *args, **options):
        try:
            symbols = list(Security.objects.all().values_list('symbol', flat=True))
            
            if symbols:
                with open('securities.json', 'w') as f:
                    json_object = json.dumps({'symbols':symbols})
                    f.write(json_object)
                    self.stdout.write(self.style.SUCCESS('Successfully exported %s Securiy symbols' % len(symbols)))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error occured: "%s"' % e))
