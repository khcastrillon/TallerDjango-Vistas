from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement_wanted(request, id):
    measurement = get_measurement(id)
    measurementWanted = serializers.serialize('json', [measurement])
    return HttpResponse(measurementWanted, content_type='application/json')