from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_variables(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')
