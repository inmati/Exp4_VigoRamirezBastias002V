from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Appointment


# MAL FINAL ESTÁN LAS VIEWS EN FORMATO REST

def home(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'us.html')


def galery(request):
    return render(request, 'galery.html')


def weather(request):
    return render(request, 'weather.html')


def createAppointment(request):

    # Form was validated previuosly in the frontend
    if len(Appointment.objects.filter(date=request.POST.dict().get('fecha'))) < 5:

        try:
            appointment = Appointment.objects.get(
                email=request.POST.dict().get('email'))
            data = {
                'message': 'Ya tienes una cita para la fecha indicada'
            }

            return render(request, 'failure.html', data)

        except Appointment.DoesNotExist:
            appointment = Appointment(request.POST.dict().get('email'), request.POST.dict().get('nombre'), request.POST.dict().get('apellido'),
                                      int(request.POST.dict().get('fono')), request.POST.dict().get('direccion'), request.POST.dict().get('fecha'))
            appointment.save()

            data = {
                'action': 'agendada',
                'nombre': Appointment.objects.get(email=request.POST.dict().get('email')).first_name,
                'apellido': Appointment.objects.get(email=request.POST.dict().get('email')).last_name,
                'email': Appointment.objects.get(email=request.POST.dict().get('email')).email,
                'fono': Appointment.objects.get(email=request.POST.dict().get('email')).phone,
                'fecha': Appointment.objects.get(email=request.POST.dict().get('email')).date
            }

            return render(request, 'appointment.html', data)

    else:

        data = {
            'message': 'sin citas disponibles para la fecha indicada'
        }

        return render(request, 'failure.html', data)


def getAppointment(request):

    try:
        appointment = Appointment.objects.get(
            email=request.GET.dict().get('email1'))

        data = {
            'action': 'agendada',
            'nombre': appointment.first_name,
            'apellido': appointment.last_name,
            'email': appointment.email,
            'fono': appointment.phone,
            'fecha': appointment.date
        }

        return render(request, 'appointment.html', data)

    except Appointment.DoesNotExist:
        data = {
            'message': 'No tienes ninguna cita tomada'
        }
        return render(request, 'failure.html', data)


def updateAppointment(request):

    try:
        print(request.POST.dict())
        appointment = Appointment.objects.filter(
            email=request.POST.dict().get('email3'))
        appointment.update(date=request.POST.dict().get('fecha3'))
        data = {
            'action': 'actualizada',
            'nombre': appointment[0].first_name,
            'apellido': appointment[0].last_name,
            'email': appointment[0].email,
            'fono': appointment[0].phone,
            'fecha': appointment[0].date
        }
        return render(request, 'appointment.html', data)

    except Appointment.DoesNotExist:

        data = {
            'message': 'No tienes cita para la fecha indicada'
        }

        return render(request, 'failure.html', data)


def deleteAppointment(request):

    try:
        # print(request.POST.dict())
        appointment = Appointment.objects.filter(
            email=request.POST.dict().get('email2'))
        appointment.delete()
        data = {
            'message': 'Cita cancelada exitosamente'
        }
        return render(request, 'success.html', data)

    except Appointment.DoesNotExist:
        data = {
            'message': 'No existe cita para el correo indicado'
        }

        return render(request, 'failure.html', data)

# Falta crear un store procedure que elimine las citas agendadas ya expiradas
# DELETE appointments WHERE appointment.date < now();
# y llamar al procedimiento cada vez que se ejecute una función crud.


######################################################### REST API ########

# LAS SIGUIENTES FUNCIONES TIENEN LA MISMA LÓGICA QUE LAS DE ARRIBA, PERO EN ESTE CASO SE GENERAN RESPUESTAS EN FORMATO JSON
# ESTA SECCIÓN PUEDE SER TESTEADA EN POSTMAN O THUNDER CLIENT (VISUAL ESTUDIO CODE EXTENSION)
# (NO FUE NECESARIO UTILIZAR SERIALIZERS EN ESTE CASO)

@api_view(['POST'])
def createAppointment(request):

    # Form was validated previuosly in the frontend
    if len(Appointment.objects.filter(date=request.data['fecha'])) < 5:

        try:
            Appointment.objects.get(email=request.data['email'])
            data = {
                'message': 'Ya tienes una cita para la fecha indicada'
            }

            return Response(data)

        except Appointment.DoesNotExist:

            appointment = Appointment(request.data['email'], request.data['nombre'], request.data['apellido'],
                                      int(request.data['fono']), request.data['direccion'], request.data['fecha'])
            appointment.save()

            data = {
                'message': 'Cita agendada con exito'
            }
            return Response(data)

    else:

        data = {
            'message': 'Sin citas disponibles para la fecha indicada'
        }

        return Response(data)


@api_view(['GET'])
def readAppointment(request, email):

    try:
        appointment = Appointment.objects.get(email=email)
        data = {
            'action': 'agendada',
            'nombre': appointment.first_name,
            'apellido': appointment.last_name,
            'email': appointment.email,
            'fono': appointment.phone,
            'fecha': appointment.date
        }

        return Response(data)

    except Appointment.DoesNotExist:
        data = {
            'message': 'No tienes ninguna cita tomada'
        }
        return Response(data)


@api_view(['PUT'])
def updateAppointment(request, email):

    try:
        appointment = Appointment.objects.filter(email=email)
        appointment.update(date=request.data['newDate'])
        data = {
            'action': 'actualizada',
            'nombre': appointment[0].first_name,
            'apellido': appointment[0].last_name,
            'email': appointment[0].email,
            'fono': appointment[0].phone,
            'fecha': appointment[0].date
        }
        return Response(data)

    except Appointment.DoesNotExist:
        data = {
            'message': 'No tienes ninguna cita tomada'
        }
        return Response(data)

@api_view(['DELETE'])
def deleteAppointment(request, email):

    try:
        appointment = Appointment.objects.filter(email = email)
        appointment.delete()

        data = {
            'message': 'Cita cancelada con exito'
        }
        return Response(data)

    except Appointment.DoesNotExist:

        data = {
            'message' : 'No existe cita para correo indicado'
        }
        return Response(data)

