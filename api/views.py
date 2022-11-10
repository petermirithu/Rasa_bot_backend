from datetime import datetime
import json
import traceback
from rest_framework.response import Response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# parse incoming data into data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from api.enc_decryption import check_password, encode_value

from api.models import Students, Courses, Faculty, Assignments
from api.permissions import isAuthorized
from api.serializers import StudentsSerializer, CoursesSerializer, FacultySerializer, AssignmentsSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


# HTTP Statuses
statusOk = status.HTTP_200_OK
statusCreated = status.HTTP_201_CREATED
statusBadRequest = status.HTTP_400_BAD_REQUEST
statusNoContent = status.HTTP_204_NO_CONTENT
statusNotFound = status.HTTP_404_NOT_FOUND
statusExists = status.HTTP_423_LOCKED

# Create your views here.
@api_view(['POST'])
def login_user(request):    
    try:
        email = request.POST.get("email")
        password = request.POST.get("password")                
        if(email and password):
            try:
                profile = Students.objects.get(stdEmail=email)                                
                if(check_password(password, profile.stdPassword) == True):
                    now = datetime.now()
                    payload = {'email': email,'loggedinAt': now.strftime("%m/%d/%Y, %H:%M:%S")}                    
                    profile.stdToken=encode_value(payload) 
                    serialised_profile = StudentsSerializer(profile, many=False)
                    return Response(serialised_profile.data, status=statusOk)
                else:
                    return Response('Password is incorrect', status=statusBadRequest)
            except Students.DoesNotExist:                
                return Response('User is not found', status=statusNotFound)
        else:
            return Response("Make sure you provide an email and password", status=statusBadRequest)
    except:        
        print(traceback.format_exc())
        return Response("An error occured while authenticating you", status=statusBadRequest)


@api_view(['GET'])
@permission_classes([isAuthorized])
def getOneStudent(request, id):
    try:
        student = Students.objects.get(stdId=id)
        students_serializer = StudentsSerializer(student, many=False)
        return JsonResponse(students_serializer.data, safe=False)
    except Students.DoesNotExist:
        return JsonResponse("The Specific Student Record Does Not Exist.", safe=False)


@api_view(['GET'])
@permission_classes([isAuthorized])
def getAllStudents(request):
    students = Students.objects.all()
    students_serializer = StudentsSerializer(students, many=True)
    return JsonResponse(students_serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([isAuthorized])
def createStudent(request):
    student_data = {
        "stdId": request.POST.get("stdId"),
        "stdFName": request.POST.get("stdFName"),
        "stdLName": request.POST.get("stdLName"),
        "stdEmail": request.POST.get("stdEmail")
    }
    students_serializer=StudentsSerializer(data=student_data)
    if students_serializer.is_valid():
        students_serializer.save()
        return JsonResponse("Student Record Added Successfully!",safe=False)
    return JsonResponse("Failed to Add Student Record :(",safe=False)


@api_view(['PUT'])
@permission_classes([isAuthorized])
def updateStudent(request):
    student_data=JSONParser().parse(request)
    student=Students.objects.get(stdId=student_data['stdId'])
    students_serializer=StudentsSerializer(student,data=student_data)
    if students_serializer.is_valid():
        students_serializer.save()
        return JsonResponse("Updated Student Record Successfully",safe=False)
    return JsonResponse("Failed to Update Student Data:(",safe=False)

@api_view(['DELETE'])
@permission_classes([isAuthorized])
def deleteStudent(request, id):
    try:
        student=Students.objects.get(stdId=id)
        student.delete()
        return JsonResponse("Deleted Student Record Successfully",safe=False)
    except Students.DoesNotExist:
        return JsonResponse("The Specified Student Record Does Not Exist.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getOneCourse(request, id):
    try:
        course=Courses.objects.get(crsId=id)
        courses_serializer=CoursesSerializer(course,many=False)
        return JsonResponse(courses_serializer.data,safe=False)
    except Courses.DoesNotExist:
        return JsonResponse("The Specific Course Record Does Not Exist.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getAllCourses(request):
    courses = Courses.objects.all()
    courses_serializer=CoursesSerializer(courses,many=True)
    return JsonResponse(courses_serializer.data,safe=False)

@api_view(['POST'])
@permission_classes([isAuthorized])
def createCourse(request):
    course_data={
        "crsId":request.POST.get("crsId"),
        "crsName":request.POST.get("crsName"),
        "meets":request.POST.get("meets"),
        "about":request.POST.get("about"),
        "location":request.POST.get("location")
    }
    courses_serializer=CoursesSerializer(data=course_data)
    if courses_serializer.is_valid():
        courses_serializer.save()
        return JsonResponse("Course Record Added Successfully!",safe=False)
    return JsonResponse("Failed to Add Course Record :(",safe=False)

@api_view(['PUT'])
@permission_classes([isAuthorized])
def updateCourse(request):
    course_data=JSONParser().parse(request)
    course=Courses.objects.get(crsId=course_data['crsId'])
    courses_serializer=CoursesSerializer(course,data=course_data)
    if courses_serializer.is_valid():
        courses_serializer.save()
        return JsonResponse("Successfully Updated Course Record",safe=False)
    return JsonResponse("Failed to Update Course Record :(",safe=False)

@api_view(['DELETE'])
@permission_classes([isAuthorized])
def deleteCourse(request, id):
    try:
        course=Courses.objects.get(crsId=id)
        course.delete()
        return JsonResponse("Deleted Course Record Successfully",safe=False)
    except Courses.DoesNotExist:
        return JsonResponse("The Specific Course Record Does Not Exist.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getOneFaculty(request, id):
    try:
        faculty=Faculty.objects.get(ftyId=id)
        faculty_serializer=FacultySerializer(faculty,many=False)
        return JsonResponse(faculty_serializer.data,safe=False)
    except Faculty.DoesNotExist:
        return JsonResponse("The Specific Faculty Record Does Not Exist.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getAllFaculty(request):
    faculty = Faculty.objects.all()
    faculty_serializer=FacultySerializer(faculty,many=True)
    return JsonResponse(faculty_serializer.data,safe=False)

@api_view(['POST'])
@permission_classes([isAuthorized])
def createFaculty(request):
    faculty_data={
        "ftyId":request.POST.get("ftyId"),
        "ftyFName":request.POST.get("ftyFName"),
        "ftyLName":request.POST.get("ftyLName"),
        "ftyEmail":request.POST.get("ftyEmail"),
        "ftyPhone":request.POST.get("ftyPhone"),
        "ftyOffice":request.POST.get("ftyOffice")
    }
    faculty_serializer=FacultySerializer(data=faculty_data)
    if faculty_serializer.is_valid():
        faculty_serializer.save()
        return JsonResponse("Faculty Record Added Successfully!",safe=False)
    return JsonResponse("Failed to Add Faculty Record :(",safe=False)

@api_view(['PUT'])
@permission_classes([isAuthorized])
def updateFaculty(request):
    faculty_data=JSONParser().parse(request)
    faculty=Faculty.objects.get(ftyId=faculty_data['ftyId'])
    faculty_serializer=FacultySerializer(faculty,data=faculty_data)
    if faculty_serializer.is_valid():
        faculty_serializer.save()
        return JsonResponse("Successfully Updated Faculty Record",safe=False)
    return JsonResponse("Failed to Update Faculty Data :(",safe=False)


@api_view(['DELETE'])
@permission_classes([isAuthorized])
def deleteFaculty(request, id):
    try:
        faculty=Faculty.objects.get(ftyId=id)
        faculty.delete()
        return JsonResponse("Successfully Deleted Faculty Record",safe=False)
    except Faculty.DoesNotExist:
        return JsonResponse("The Specific Faculty Record Does Not Exist.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getOneAssignment(request, id):
    try:
        assignment=Assignments.objects.get(asgmtId=id)
        assignments_serializer=AssignmentsSerializer(assignment,many=False)
        return JsonResponse(assignments_serializer.data,safe=False)
    except Assignments.DoesNotExist:
        return JsonResponse("The Specific Assignment Record Does Not Exist.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getCourseAssignments(request, crsId):
    try:
        assignments=Assignments.objects.filter(crsId=crsId)
        assignments_serializer=AssignmentsSerializer(assignments,many=True)
        return JsonResponse(assignments_serializer.data,safe=False)
    except Assignments.DoesNotExist:
        return JsonResponse("No assignments for this course.", safe=False)

@api_view(['GET'])
@permission_classes([isAuthorized])
def getAllAssignments(request):
    assignments = Assignments.objects.all()
    assignments_serializer=AssignmentsSerializer(assignments,many=True)
    return JsonResponse(assignments_serializer.data,safe=False)

@api_view(['POST'])
@permission_classes([isAuthorized])
def createAssignment(request):
    assignment_data={
        "asgmtId":request.POST.get("asgmtId"),
        "crsId":request.POST.get("crsId"),
        "asgmtName":request.POST.get("asgmtName"),
        "dateGiven":request.POST.get("dateGiven"),
        "dateDue":request.POST.get("dateDue"),
        "attempts":request.POST.get("attempts")
    }    
    assignments_serializer=AssignmentsSerializer(data=assignment_data)    
    if assignments_serializer.is_valid():        
        assignments_serializer.save()
        return JsonResponse("Assignments Data Added Successfully!",safe=False)
    return JsonResponse("Failed to Add Assignments Data :(",safe=False)

@api_view(['PUT'])
@permission_classes([isAuthorized])
def updateAssignment(request):
    assignment_data=JSONParser().parse(request)
    assignment=Assignments.objects.get(asgmtId=assignment_data['asgmtId'])
    assignments_serializer=AssignmentsSerializer(assignment,data=assignment_data)    
    if assignments_serializer.is_valid():
        assignments_serializer.save()
        return JsonResponse("Updated Assignments Successfully",safe=False)
    return JsonResponse("Failed to Update Assignments :(",safe=False)

@api_view(['DELETE'])
@permission_classes([isAuthorized])
def deleteAssignment(request, id):
    try:
        assignment=Assignments.objects.get(asgmtId=id)
        assignment.delete()
        return JsonResponse("Deleted Assignment Successfully",safe=False)
    except Assignments.DoesNotExist:
        return JsonResponse("The Specific Assignment Record Does Not Exist.", safe=False)