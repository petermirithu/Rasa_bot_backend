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
        if(id!=0):
            student=Students.objects.get(stdId=id)
            students_serializer=StudentsSerializer(student,many=False)
            return JsonResponse(students_serializer.data,safe=False)
        else:
            students = Students.objects.all()
            students_serializer=StudentsSerializer(students,many=True)
            return JsonResponse(students_serializer.data,safe=False)
    elif request.method=='POST':
        student_data={
            "stdId":request.POST.get("stdId"),
            "stdFName":request.POST.get("stdFName"),
            "stdLName":request.POST.get("stdLName"),
            "stdEmail":request.POST.get("stdEmail")
        }
        students_serializer=StudentsSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Student Record Added Successfully!",safe=False)
        return JsonResponse("Failed to Add Student Record :(",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Students.objects.get(stdId=student_data['stdId'])
        students_serializer=StudentsSerializer(student,data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Student Record Successfully",safe=False)
        return JsonResponse("Failed to Update Student Data:(",safe=False)
    elif request.method=='DELETE':
        student=Students.objects.get(stdId=id)
        student.delete()
        return JsonResponse("Deleted Student Record Successfully",safe=False)

@csrf_exempt
def courseApi(request, id=0):
    if request.method=='GET':
        if(id!=0):
            course=Courses.objects.get(crsId=id)
            courses_serializer=CoursesSerializer(course,many=False)
            return JsonResponse(courses_serializer.data,safe=False)
        else:
            courses = Courses.objects.all()
            courses_serializer=CoursesSerializer(courses,many=True)
            return JsonResponse(courses_serializer.data,safe=False)
    elif request.method=='POST':
        course_data={
            "crsId":request.POST.get("crsId"),
            "crsName":request.POST.get("crsName"),
            "meets":request.POST.get("meets")
        }
        courses_serializer=CoursesSerializer(data=course_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse("Course Record Added Successfully!",safe=False)
        return JsonResponse("Failed to Add Course Record :(",safe=False)
    elif request.method=='PUT':
        course_data=JSONParser().parse(request)
        course=Courses.objects.get(crsId=course_data['crsId'])
        courses_serializer=CoursesSerializer(course,data=course_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse("Successfully Updated Course Record",safe=False)
        return JsonResponse("Failed to Update Course Record :(",safe=False)
    elif request.method=='DELETE':
        course=Courses.objects.get(crsId=id)
        course.delete()
        return JsonResponse("Deleted Course Record Successfully",safe=False)

@csrf_exempt
def facultyApi(request, id=0):
    if request.method=='GET':
        if(id!=0):
            faculty=Faculty.objects.get(ftyId=id)
            faculty_serializer=FacultySerializer(faculty,many=False)
            return JsonResponse(faculty_serializer.data,safe=False)
        else:
            faculty = Faculty.objects.all()
            faculty_serializer=FacultySerializer(faculty,many=True)
            return JsonResponse(faculty_serializer.data,safe=False)
    elif request.method=='POST':
        faculty_data={
            "ftyId":request.POST.get("ftyId"),
            "ftyFName":request.POST.get("ftyFName"),
            "ftyLName":request.POST.get("ftyLName")
        }
        faculty_serializer=FacultySerializer(data=faculty_data)
        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return JsonResponse("Faculty Record Added Successfully!",safe=False)
        return JsonResponse("Failed to Add Faculty Record :(",safe=False)
    elif request.method=='PUT':
        faculty_data=JSONParser().parse(request)
        faculty=Faculty.objects.get(ftyId=faculty_data['ftyId'])
        faculty_serializer=FacultySerializer(faculty,data=faculty_data)
        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return JsonResponse("Successfully Updated Faculty Record",safe=False)
        return JsonResponse("Failed to Update Faculty Data :(",safe=False)
    elif request.method=='DELETE':
        faculty=Faculty.objects.get(ftyId=id)
        faculty.delete()
        return JsonResponse("Successfully Deleted Faculty Record",safe=False)

#cant get
@csrf_exempt
def assignmentApi(request, id=0):
    if request.method=='GET':
        if(id!=0):
            assignment=Assignments.objects.get(asgmtId=id)
            assignments_serializer=AssignmentsSerializer(assignment,many=False)
            return JsonResponse(assignments_serializer.data,safe=False)
        else:
            assignments = Assignments.objects.all()
            assignments_serializer=AssignmentsSerializer(assignments,many=True)
            return JsonResponse(assignments_serializer.data,safe=False)
    elif request.method=='POST':
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
    elif request.method=='PUT':
        assignment_data=JSONParser().parse(request)
        assignment=Assignments.objects.get(asgmtId=assignment_data['asgmtId'])
        assignments_serializer=AssignmentsSerializer(assignment,data=assignment_data)
        if assignments_serializer.is_valid():
            assignments_serializer.save()
            return JsonResponse("Updated Assignments Successfully",safe=False)
        return JsonResponse("Failed to Update Assignments :(",safe=False)
    elif request.method=='DELETE':
        assignment=Assignments.objects.get(asgmtId=id)
        assignment.delete()
        return JsonResponse("Deleted Assignment Successfully",safe=False)

