from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from sistemas.models import LogEntry


class Command(BaseCommand):
    help = 'Import logs from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date_str = row['Date']
                time_str = row['Time']
                formatted_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                log_entry = LogEntry(
                    date=formatted_date,
                    time=time_str,
                    level=row['Level'],
                    process=row['Process'],
                    component=row['Component'],
                    content=row['Content'],
                    event_id=row['EventId'],
                    event_template=row['EventTemplate']
                )
                log_entry.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully imported LOG ID {log_entry.line_id}'))