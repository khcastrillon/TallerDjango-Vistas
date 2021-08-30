from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(id):
    measurement = Measurement.objects.get(pk=id)
    return measurement

def delete_measurement(id):
    Measurement.objects.get(pk=id).delete()

def update_measurement(id,pValue):
    Measurement.objects.filter(pk=id).update(value=pValue)
    updatedMeasurement = get_measurement(id)
    return updatedMeasurement
