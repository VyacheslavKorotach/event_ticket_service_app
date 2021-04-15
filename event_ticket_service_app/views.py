from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    # return HttpResponse("Hello, world. You're at the event service index.")
    return service_selector(request)


def service_selector(request):
    template = loader.get_template('service_selector.html')
    sent = False
    context = {
        'sent': sent,
    }
    return HttpResponse(template.render(context, request))
