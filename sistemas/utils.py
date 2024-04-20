from django.db.models import Count
from django.db.models.functions import TruncHour
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import RiskLog, LogEntry
from django.core.mail import send_mail


def log_event(username, ip_address, risk_level, description):
    RiskLog.objects.create(
        username=username,
        ip_address=ip_address,
        risk_level=risk_level,
        description=description,
    )


def count_specific_logs(description):
    return RiskLog.objects.filter(description=description).count()


def get_logs_by_hour():
    logs_by_hour =(
        RiskLog.objects
        .annotate(hour=TruncHour('timestamp'))
        .values('hour')
        .annotate(count=Count('id'))
    )
    return logs_by_hour


def count_log_entries_by_risk():
    level_mapping = {
        'WARNING': 'low',   # Mapped to Riesgo bajo
        'ERROR': 'medium',  # Mapped to Riesgo medio
        'FATAL': 'high',    # Mapped to Riesgo alto
    }

    # Initialize counts
    risk_counts = {'low': 0, 'medium': 0, 'high': 0}

    # Iterate through each log entry and increment the appropriate risk count
    for entry in LogEntry.objects.all():
        risk_level = level_mapping.get(entry.level, None)
        if risk_level:
            risk_counts[risk_level] += 1
    print(risk_counts)
    return risk_counts



