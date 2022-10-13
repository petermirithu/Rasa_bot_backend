from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser #parse incoming data into data model
from django.http.response import JsonResponse

from api.models import Students, Courses, Faculty, Assignments
from api.serializers import StudentsSerializer, CoursesSerializer, FacultySerializer, AssignmentsSerializer


# Create your views here.
# Render to the frontpage lesgooo!

@csrf_exempt
def studentApi(request, id=0):
    if request.method=='GET':
        students = Students.objects.all()
        students_serializer=StudentsSerializer(students,many=True)
        return JsonResponse(students_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        students_serializer=StudentsSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Data Added Successfully!",safe=False)
        return JsonResponse("Failed to Add Data :(",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Students.objects.get(stdId=student_data['stdId'])
        students_serializer=StudentsSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update :(",safe=False)
    elif request.method=='DELETE':
        student=Students.objects.get(stdId=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)

