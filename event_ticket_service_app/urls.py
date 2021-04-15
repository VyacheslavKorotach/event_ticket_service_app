"""event_ticket_service_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.urls import path
# from . import views as local_views
from django.urls import include, path
from . import views

urlpatterns = [
    path('event_service/', include('event_service.urls')),
    path('ticket_service/', include('ticket_service.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('event_service/', local_views.index, name='index'),
]
