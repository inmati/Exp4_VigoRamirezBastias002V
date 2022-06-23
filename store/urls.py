from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("galery", views.galery, name="galery"),
    path("us", views.us, name="us"),
    path("weather", views.weather, name="weather"),
    path("appointment", views.createAppointment, name="appointment"),
    path("get-appointment", views.getAppointment, name="get-appointment"),
    path("update-appointment", views.updateAppointment, name="update-appointment"),
    path("delete-appointment", views.deleteAppointment, name="delete-appointment")
]
