from rest_framework import serializers
from api.models import Students, Courses, Faculty, Assignments, StudentsCourses, FacultyCourses

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('stdId', 'stdFName', 'stdLName', 'stdEmail', 'stdToken')

class StudentsCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentsCourses
        fields=('stdId', 'crsId', 'sdcsId')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('crsId', 'crsName', 'meets')

class FacultyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=FacultyCourses
        fields=('ftyId', 'crsId', 'fycsId')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('ftyId', 'ftyFName', 'ftyLName')

class AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assignments
        fields=('asgmtId', 'crsId', 'asgmtName', 'dateGiven', 'dateDue', 'attempts')