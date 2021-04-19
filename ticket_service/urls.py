from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='ticket_service'),
    path('details/', views.ticket_details),
]