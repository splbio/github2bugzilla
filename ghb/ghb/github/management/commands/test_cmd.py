import os
import logging
import pprint

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        print "Inside test_cmd!"
        return

