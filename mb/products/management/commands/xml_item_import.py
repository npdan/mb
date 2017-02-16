from django.core.management.base import BaseCommand, CommandError
from products.models import do_import
import argparse


class Command(BaseCommand):
    help = 'Update items with data read from XML file. '

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        print options['f'], dir(options['f'])
        self.stdout.write('Importing data from %s' % (options['f']))
        errors = do_import(options['f'])
        if errors:
            for field_errors in errors:
                for error in field_errors:
                    self.stdout.write(
                        '%s: %s' % (
                            self.style.ERROR(error[1]),
                            self.style.ERROR(error[2])))
        else:
            self.stdout.write(self.style.SUCCESS('Successfully Imported'))
