from os import stat
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from persona_app import serializers
from persona_app.models import Persona
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from persona_app.serializers import PersonaSerializer

@api_view(['GET'])
def obtenerPerfil(request, id):
    try:
        perfil = Persona.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializado = PersonaSerializer(perfil)

    return Response(serializado.data)
# Create your views here.


# PUT = actualizar, DELETE = borrar
@api_view(['PUT','DELETE'])
def modificarPersona(request, id):
    try:
        persona = Persona.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

#verificar si es actualizar (actualizar)
    if request.method == 'PUT':
        serializado = PersonaSerializer(persona, data=request.data)
        if serializado.is_valid():
           serializado.save()
           return Response(serializado.errors, status=status.HTTP_200_OK)

        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

#verificar si es eliminar
    if request.method == 'DELETE':
       persona.delete()
       return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
def obtenerPersonas(request):
    if request.method == 'GET':
        persona_obtenidas = Persona.objects.all()
        serializado = PersonaSerializer(persona_obtenidas, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        deserializado = PersonaSerializer(data=request.data)

        if deserializado.is_valid():

            deserializado.save()
            return Response(deserializado.data, status=status.HTTP_200_OK)

        else:
            return Response(deserializado.errors,status=status.HTTP_400_BAD_REQUEST)
