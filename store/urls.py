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
    path("delete-appointment", views.deleteAppointment, name="delete-appointment"),
    # DE AQUÍ PARA ABAJO LAS URLS SON PARA COMUNICARSE CON LA API REST #
    path("appointment/create", views.createAppointment, name="create-appointment"),
    path("appointment/<str:email>/read", views.readAppointment, name="read-appointment"),
    path("appointment/<str:email>/update", views.updateAppointment, name="update-appointment"),
    path("appointment/<str:email>/delete", views.deleteAppointment, name="delete-appointment")
]
