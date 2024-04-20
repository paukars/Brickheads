"""
URL configuration for Hackathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistemas.forms import CustomAuthenticationForm
from django.contrib.auth import views as auth_views
from sistemas.views import dashboard_view
from sistemas.views import comunicacion_view
from sistemas.views import registro_view
from sistemas.views import tickets_view, tickets_view5,tickets_view6, tickets_view1
from sistemas.views import tickets_view2, tickets_view3, tickets_view4
from sistemas.views import send_test_email, grafica1, grafica2


urlpatterns = [
    path('', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('detalles/', tickets_view, name='detalle_ticket'),
    path('send-email/', send_test_email ),
    path('dashboards/contenido2.html', grafica2),
    path('dashboards/contenido1.html', grafica1),
    path('detalles/contenido1.html',tickets_view1),
    path('detalles/contenido2.html',tickets_view2),
    path('detalles/contenido3.html',tickets_view3),
    path('detalles/contenido4.html',tickets_view4),
    path('detalles/contenido5.html',tickets_view5),
    path('detalles/contenido6.html',tickets_view6),
    path('tickets/', registro_view, name='tickets'),
    path('comunicacion/',comunicacion_view, name = 'comunicacion'),
    path('dashboards/', dashboard_view, name='dashboard'),
    path('admin/', admin.site.urls, name = admin),
]
