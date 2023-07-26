from rest_framework import serializers
from myapi.models import StudentModel

class StudentSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)

