from django.urls import re_path, path
from api import views

urlpatterns=[
    # re_path(r'^student$', views.studentApi),
    # re_path(r'^student/([0-9]+)$', views.studentApi),
    path('getOneStudent/<str:id>', views.getOneStudent),
    path('getAllStudents', views.getAllStudents),
    path('createStudent', views.createStudent),
    path('updateStudent', views.updateStudent),
    path('deleteStudent/<str:id>', views.deleteStudent),
    # re_path(r'^course$', views.courseApi),
    # re_path(r'^course/([0-9]+)$', views.courseApi),
    path('getOneCourse/<str:id>', views.getOneCourse),
    path('getAllCourses', views.getAllCourses),
    path('createCourse', views.createCourse),
    path('updateCourse', views.updateCourse),
    path('deleteCourse/<str:id>', views.deleteCourse),
    # re_path(r'^faculty$', views.facultyApi),
    # re_path(r'^faculty/([0-9]+)$', views.facultyApi),
    path('getOneFaculty/<str:id>', views.getOneFaculty),
    path('getAllFaculty', views.getAllFaculty),
    path('createFaculty', views.createFaculty),
    path('updateFaculty', views.updateFaculty),
    path('deleteFaculty/<str:id>', views.deleteFaculty),
    # re_path(r'^assignment$', views.assignmentApi),
    # re_path(r'^assignment/([0-9]+)$', views.assignmentApi)
    path('getOneAssignment/<str:id>', views.getOneAssignment),
    path('getAllAssignments', views.getAllAssignments),
    path('createAssignment', views.createAssignment),
    path('updateAssignment', views.updateAssignment),
    path('deleteAssignment/<str:id>', views.deleteAssignment),
]