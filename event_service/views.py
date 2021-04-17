from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import PatientSelection


def index(request):
    # return HttpResponse("Hello, world. You're at the event service index.")
    return event_service_list(request)


def event_service_list(request):
    # template = loader.get_template('event_service/event_service_list.html')
    template = loader.get_template('event_service/event_service_list.html')
    sent = False
    context = {
        'sent': sent,
    }
    return HttpResponse(template.render(context, request))


def event_details(request):
    template = loader.get_template('event_service/event_details.html')
    sent = False
    context = {
        'sent': sent,
    }
    return HttpResponse(template.render(context, request))


def create_new(request):
    template = loader.get_template('event_service/create_new.html')
    sent = False
    context = {
        'sent': sent,
    }
    return HttpResponse(template.render(context, request))
