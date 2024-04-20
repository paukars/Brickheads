from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomAuthenticationForm
from .models import CustomUser
from .models import RiskLog
from .utils import count_specific_logs, count_log_entries_by_risk
from .utils import get_logs_by_hour
from .models import LogEntry
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.


def login_view(request):
    return render(request, 'registration/login.html', )


def dashboard_view(request):
    low_risk_count=RiskLog.objects.filter(risk_level='low').count()
    medium_risk_count=RiskLog.objects.filter(risk_level='medium').count()
    high_risk_count=RiskLog.objects.filter(risk_level='high').count()

    staff_access_count = count_specific_logs('Staff accedio a su cuenta')
    staff_failed_login = count_specific_logs('Intento de inicio de sesion a una cuenta staff')
    user_failed_login = count_specific_logs('Intento de inicio de sesion a una cuenta')

    logs_data = get_logs_by_hour()
    hours = [log['hour'].strftime('%Y - %m -%d %H:%M') for log in logs_data]
    counts = [log['count'] for log in logs_data]
    recent_logs = RiskLog.objects.all().order_by('-timestamp')[:10]

    log_entry_counts = count_log_entries_by_risk()
    context = {
        'low_risk_count': low_risk_count + log_entry_counts['low'],
        'medium_risk_count': medium_risk_count + log_entry_counts['medium'],
        'high_risk_count': high_risk_count + log_entry_counts['high'],
        'staff_access_count': staff_access_count,
        'staff_failed_login': staff_failed_login,
        'user_failed_login': user_failed_login,
        'hours': hours,
        'counts': counts,
        'recent_logs': recent_logs,
    }

    return render(request, 'dashboard2.html',context)


def comunicacion_view(request):
    return render(request, 'comunicacion.html')


def registro_view(request):
    risk_logs = RiskLog.objects.all().order_by('-timestamp')[:]
    log_entry = LogEntry.objects.filter(level__in=['WARNING', 'ERROR', 'FATAL'])
    return render(request, 'tickets1.html', {'risk_logs': risk_logs, 'log_entry': log_entry})


def tickets_view(request):
    return render(request,'tickedindividual/tickedindividual.html')


def tickets_view1(request):
    return render(request,'tickedindividual/contenido1.html')


def tickets_view2(request):
    return render(request,'tickedindividual/contenido2.html')


def tickets_view3(request):
    return render(request,'tickedindividual/contenido3.html')


def tickets_view4(request):
    return render(request, 'tickedindividual/contenido4.html')


def tickets_view5(request):
    return render(request,'tickedindividual/contenido5.html')


def tickets_view6(request):
    return render(request,'tickedindividual/contenido6.html')


def send_test_email(request):
    subject = 'Hello from Django'
    message = 'This is a test email sent from a Django application.'
    email_from = 'lobohackathon2024@gmail.com'
    recipient_list = ['paulsoar19@gmail.com']

    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("Email sent successfully")


def grafica1(request):
    low_risk_count=RiskLog.objects.filter(risk_level='low').count()
    medium_risk_count=RiskLog.objects.filter(risk_level='medium').count()
    high_risk_count=RiskLog.objects.filter(risk_level='high').count()

    staff_access_count = count_specific_logs('Staff accedio a su cuenta')
    staff_failed_login = count_specific_logs('Intento de inicio de sesion a una cuenta staff')
    user_failed_login = count_specific_logs('Intento de inicio de sesion a una cuenta')

    logs_data = get_logs_by_hour()
    hours = [log['hour'].strftime('%Y - %m -%d %H:%M') for log in logs_data]
    counts = [log['count'] for log in logs_data]
    recent_logs = RiskLog.objects.all().order_by('-timestamp')[:10]
    log_entry_counts = count_log_entries_by_risk()
    context = {
        'low_risk_count': low_risk_count + log_entry_counts['low'],
        'medium_risk_count': medium_risk_count + log_entry_counts['medium'],
        'high_risk_count': high_risk_count + log_entry_counts['high'],
        'staff_access_count': staff_access_count,
        'staff_failed_login': staff_failed_login,
        'user_failed_login': user_failed_login,
        'hours': hours,
        'counts': counts,
        'recent_logs': recent_logs,
    }
    return render(request,'contenido1.html', context)


def grafica2(request):
    low_risk_count=RiskLog.objects.filter(risk_level='low').count()
    medium_risk_count=RiskLog.objects.filter(risk_level='medium').count()
    high_risk_count=RiskLog.objects.filter(risk_level='high').count()

    staff_access_count = count_specific_logs('Staff accedio a su cuenta')
    staff_failed_login = count_specific_logs('Intento de inicio de sesion a una cuenta staff')
    user_failed_login = count_specific_logs('Intento de inicio de sesion a una cuenta')

    logs_data = get_logs_by_hour()
    hours = [log['hour'].strftime('%Y - %m -%d %H:%M') for log in logs_data]
    counts = [log['count'] for log in logs_data]
    recent_logs = RiskLog.objects.all().order_by('-timestamp')[:10]

    context = {
        'low_risk_count': low_risk_count,
        'medium_risk_count': medium_risk_count,
        'high_risk_count': high_risk_count,
        'staff_access_count': staff_access_count,
        'staff_failed_login': staff_failed_login,
        'user_failed_login': user_failed_login,
        'hours': hours,
        'counts': counts,
        'recent_logs': recent_logs,
    }
    return render(request,'contenido2.html', context)
