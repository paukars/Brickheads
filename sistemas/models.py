from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, verbose_name='Nombre')
    last_name = models.CharField(max_length=20, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo electronico')
    username = models.CharField(verbose_name='Usuario', max_length=20, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class FailedLoginAttempt(models.Model):
    username = models.CharField(max_length=20, verbose_name='Usuario')
    ip_address = models.GenericIPAddressField(verbose_name='IP')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    def __str__(self):
        return f"{self.username} at {self.timestamp}"

    class Meta:
        verbose_name = 'Registro de intentos fallidos de inicio de sesion'
        verbose_name_plural = 'Registros de intentos fallidos de inicio de sesion'


class RiskLog(models.Model):
    RISK_LEVEL_CHOICES = (
        ('low', 'Riesgo bajo'),
        ('medium', 'Riesgo medio'),
        ('high', 'Riesgo alto'),
    )

    STATUS_CHOICES = (
        ('Pending', 'Pendiente'),
        ('Assigned', 'Asignado'),
        ('Resuelto','Reasignado'),
    )

    username = models.CharField(max_length=20, verbose_name='Usuario')
    ip_address = models.GenericIPAddressField(verbose_name='IP')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    risk_level = models.CharField(choices=RISK_LEVEL_CHOICES, verbose_name='Nivel de riesgo')
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unassigned', verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Logs de riesgos'
        verbose_name = 'Log de riesgo'

    def __str__(self):
        return f"{self.risk_level} risk at {self.timestamp} by {self.username}"


class LogEntry(models.Model):
    line_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.CharField(max_length=12)
    level = models.CharField(max_length=255)
    process = models.CharField(max_length=255)
    component = models.CharField(max_length=255)
    content = models.TextField()
    event_id = models.CharField(max_length=50)
    event_template = models.TextField()


    @property
    def risk_level(self):
        level_mapping = {
            'WARNING': 'Riesgo bajo',
            'ERROR': 'Riesgo medio',
            'FATAL': 'Riesgo alto',
        }
        return level_mapping.get(self.level,'unknown')
    def __str__(self):
        return f"{self.line_id} - {self.level}"




