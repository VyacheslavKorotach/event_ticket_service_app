from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='event_service'),
    path('details/', views.event_details),
    path('create_new/', views.create_new, name='create_new'),
]
