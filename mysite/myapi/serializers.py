from rest_framework import serializers
from myapi.models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        models = StudentModel
        fields = '__all__'