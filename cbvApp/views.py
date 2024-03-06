from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StudentCBV
from .serializers import StudentCBVSerializer


# Create your views here.
class StudentListView(APIView):
    def get(self, request):
        student = StudentCBV.objects.all()
        serializer = StudentCBVSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentCBVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return StudentCBV.objects.get(pk=pk).first()
        except StudentCBV.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        student_serializer = StudentCBVSerializer(student)
        return Response(student_serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        student_serializer = StudentCBVSerializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
