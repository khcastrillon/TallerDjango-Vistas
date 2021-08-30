from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement
from .logic.logic_measurements import delete_measurement
from .logic.logic_measurements import update_measurement
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_wanted_measurement(request, id):
    measurement = get_measurement(id)
    wantedMeasurement = serializers.serialize('json', [measurement])
    return HttpResponse(wantedMeasurement, content_type='application/json')

def delete_wanted_measurement(requerst, id):
    delete_measurement(id)
    return HttpResponse(("Deleted measurement: ", id))

def update_wanted_measurement(request, id, value):
    update = update_measurement(id, value)
    updatedMeasurement = serializers.serialize('json', [update])
    return HttpResponse(updatedMeasurement, content_type='application/json')
