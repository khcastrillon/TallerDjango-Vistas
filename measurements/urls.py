from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<int:id>/', views.get_wanted_measurement, name='wantedMeasurament'),
    path('delete/<int:id>/', views.delete_wanted_measurement, name='deletedMeasutement'),
    path('update/<int:id>-<value>/', views.update_wanted_measurement, name='updatedMeasutement')
]
