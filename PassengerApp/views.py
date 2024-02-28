from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from PassengerApp.models import Passenger
from PassengerApp.serializers import PassengerSerializer
from fbvApp.models import Student
from fbvApp.serializers import StudentSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def create_list_passenger(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        passenger_serializer = PassengerSerializer(passengers, many=True)
        return Response(passenger_serializer.data)
    if request.method == 'POST':
        passenger_serializer = PassengerSerializer(data=request.data)
        if passenger_serializer.is_valid():
            passenger_serializer.save()
            return Response(passenger_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(passenger_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_passenger(request, pk):
    try:
        passenger = Passenger.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        passenger_serializer = PassengerSerializer(passenger)
        return Response(passenger_serializer.data)
    if request.method == 'PUT':
        passenger_serializer = PassengerSerializer(passenger,
                                                   data=request.data)
        if passenger_serializer.is_valid():
            passenger_serializer.save()
            return Response(passenger_serializer.data)
        return Response(passenger_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
