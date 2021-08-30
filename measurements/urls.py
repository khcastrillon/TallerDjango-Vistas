from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<int:id>', views.get_measurement_wanted, name='wantedMeasurament' )
]
