from rest_framework import serializers
from api.models import Students, Courses, Faculty, Assignments

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        exclude=("stdPassword",)

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields="__all__"

class AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assignments
        fields="__all__"