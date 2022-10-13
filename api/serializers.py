from rest_framework import serializers
from api.models import Students, Courses, Faculty, Assignments

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('stdId', 'stdFName', 'stdLName', 'stdEmail')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('crsId', 'crsName', 'meets')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('ftyId', 'ftyFName', 'ftyLName')

class AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assignments
        fields=('asgmtId', 'crsId', 'asgmtName', 'dateGiven', 'dateDue', 'attempts')