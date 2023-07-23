from http.client import HTTPResponse
import math
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render
from django.http import JsonResponse

from models import Student
from serializers import StudentSerializer

#function-based views (FBV)
def hello_view(request):
    
    data = {"message": "hello"}
    return JsonResponse(data)

#class-based views (CBV)
class StudentView(generics.GenericAPIView):
    serializerStudentClass = StudentSerializer
    querySet = Student.object.all


    def get(self, request):

        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")

        student = Student.objects.all()
        totalStudent = student.count()

        if search_param:
            student = Student.objects.filter(name__icontains=search_param)
        serializer = self.serializerStudentClass(student[start_num, end_num], many=True)

        return Response({
            "status": "success",
            "total": "total_students",
            "page": page_num,
            "last_page": math.ceil(totalStudent/ limit_num),
            "students": serializer.data
        })


    
    def post(self, request):
        return 1