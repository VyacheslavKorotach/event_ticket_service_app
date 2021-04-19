from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import PatientSelection


def index(request):
    # return HttpResponse("Hello, world. You're at the event service index.")
    return ticket_service_list(request)


def ticket_service_list(request):
    template = loader.get_template('ticket_service/ticket_service_list.html')
    sent = False
    form = PatientSelection()
    context = {
        'sent': sent,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def ticket_details(request):
    template = loader.get_template('ticket_service/ticket_details.html')
    sent = False
    context = {
        'sent': sent,
    }
    return HttpResponse(template.render(context, request))
