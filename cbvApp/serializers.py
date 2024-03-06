from rest_framework.serializers import ModelSerializer

from cbvApp.models import StudentCBV


class StudentCBVSerializer(ModelSerializer):
    class Meta:
        model = StudentCBV
        fields = '__all__'
