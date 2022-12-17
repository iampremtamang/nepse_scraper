import json
from django.core.management.base import BaseCommand, CommandError

from share.models import SecurityDetail


class Command(BaseCommand):
    help = 'Run update security details'
    
    def handle(self, *args, **options):
        try:
            with open('fetched_results.json', 'r') as f:
                json_object = json.load(f)
                
                if not json_object:
                    self.stdout.write(self.style.ERROR('No data in files to update' ))
                else:
                    for record in json_object['data']:
                        if SecurityDetail.check_symbol_exists(record['symbol']):
                            SecurityDetail.update_symbol_info(record['symbol'], record)
                        else:
                            SecurityDetail.create(record)
                            pass
                    self.stdout.write(self.style.SUCCESS('Successfully updated security details' ))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error occured: "%s"' % e))
