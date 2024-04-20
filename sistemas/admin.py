from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import FailedLoginAttempt
from .models import RiskLog
from .models import LogEntry
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','username', 'first_name','last_name','is_staff')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_nane', 'last_name')})
    )


@admin.register(LogEntry)
class LogEntry(admin.ModelAdmin):
    list_display = ('line_id','date','level','event_template')
    list_filter = ('level',)



@admin.register(FailedLoginAttempt)
class FailedLoginAttempt(admin.ModelAdmin):
    list_display = ('username','ip_address', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('username', 'ip_address')


@admin.register(RiskLog)
class RiskLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'risk_level', 'timestamp', 'description','status')
    list_filter = ('risk_level','timestamp','status')
    search_fields = ('username', 'description')


admin.site.register(CustomUser, CustomUserAdmin)
