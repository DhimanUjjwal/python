from http.client import HTTPResponse
import math
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from myapi.models import StudentModel
from myapi.serializers import StudentSerializer

#function-based views (FBV)
def hello_view(request):
    
    data = {"message": "hello"}
    return JsonResponse(data)

#class-based views (CBV)
class StudentView(generics.GenericAPIView):
    serializerStudentClass = StudentSerializer
    querySet = StudentModel.objects.all()   


    def get(self, request):
        
        
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")

        student = StudentModel.objects.all()
        return Response({
            "Student": student
        })
        totalStudent = student.count()
        

        if search_param:
            student = StudentModel.objects.filter(name__icontains=search_param)
            if student:    
                serializer = self.serializerStudentClass(student[start_num, end_num], many=True)  # type: ignore
                if serializer:
                    return Response({
                        "status": "success",
                        "total": "total_students",
                        "page": page_num,
                        "last_page": math.ceil(totalStudent/ limit_num),
                        "students": serializer.data
                    })
                else:
                    return Response({
                        "Status": "no ser"
                    })
            else:
                return Response({
                    "status": "fail",
                    "message": "No student found"
                }, status=status.HTTP_404_NOT_FOUND)

    
    def post(self, request,pk=0):

        serializer = self.serializerStudentClass(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        # serializer = self.serializerStudentClass(data=request.data)
        # return JsonResponse({"Hello": serializer}, status=status.HTTP_200_OK)

        # if serializer.is_valid():
           
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # serializer = self.serializerStudentClass(data=request.data)
        # temp = {'Helssslo, world!':serializer}
        # return JsonResponse(temp) 
        # if serializer:
           
        #     if serializer.is_valid():
        #         return HttpResponse("Hello, world!")
        #         data = serializer.validated_data
        #         json_data = JSONRenderer().render(data)
        #         return HttpResponse(json_data, content_type='application/json')
        #     else:
        #         return HttpResponse("Helssslo, world!")   
        #         errors = serializer.errors
        # else:
        #     return HttpResponse({
        #         "status": "fail",
        #         "message": "Valid request data"
        #     }, status=status.HTTP_404_NOT_FOUND)
    # ...