from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, FailedLoginAttempt
from django.contrib.auth import authenticate, get_user_model
from django.utils import timezone
from .utils import log_event
from django.contrib.auth.models import User


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        ip_address = self.request.META.get('REMOTE_ADDR', '')

        if not user:
            existing_user=User.objects.filter(username=username, is_staff=True).first()
            messages.error(self.request,'Usuario o contrasena incorrecta')
            if existing_user:
                log_event(username, ip_address, "high", 'Intento de inicio de sesion a una cuenta staff')
            else:
                FailedLoginAttempt.objects.create(username = username, ip_address = ip_address, timestamp = timezone.now())
                log_event(username, ip_address, "low", 'Intento de inicio de sesion a una cuenta')
            FailedLoginAttempt.objects.create(username=username, ip_address=ip_address, timestamp=timezone.now())
            raise forms.ValidationError("Usuario o contrasena incorrecta. Vuelva a intentarlo")
        else:
            self.user_cache = user
            if user.is_staff:
                log_event(user.username, ip_address,"low", 'Staff accedio a su cuenta')
        return self.cleaned_data
