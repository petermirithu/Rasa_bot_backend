from django.urls import re_path, path
from api import views

urlpatterns=[
    path('getOneStudent/<str:id>', views.getOneStudent),
    path('getAllStudents', views.getAllStudents),
    path('createStudent', views.createStudent),
    path('updateStudent', views.updateStudent),
    path('deleteStudent/<str:id>', views.deleteStudent),

    path('getOneStudentCourse/<str:id>', views.getOneStudentCourse),
    path('getAllStudentsCourses', views.getAllStudentsCourses),
    path('createStudentCourse', views.createStudentCourse),
    path('updateStudentCourse', views.updateStudentCourse),
    path('deleteStudentCourse/<str:id>', views.deleteStudentCourse),

    path('getOneCourse/<str:id>', views.getOneCourse),
    path('getAllCourses', views.getAllCourses),
    path('createCourse', views.createCourse),
    path('updateCourse', views.updateCourse),
    path('deleteCourse/<str:id>', views.deleteCourse),

    path('getOneFacultyCourse/<str:id>', views.getOneFacultyCourse),
    path('getAllFacultyCourses', views.getAllFacultyCourses),
    path('createFacultyCourse', views.createFacultyCourse),
    path('updateFacultyCourse', views.updateFacultyCourse),
    path('deleteFacultyCourse/<str:id>', views.deleteFacultyCourse),

    path('getOneFaculty/<str:id>', views.getOneFaculty),
    path('getAllFaculty', views.getAllFaculty),
    path('createFaculty', views.createFaculty),
    path('updateFaculty', views.updateFaculty),
    path('deleteFaculty/<str:id>', views.deleteFaculty),

    path('getOneAssignment/<str:id>', views.getOneAssignment),
    path('getCourseAssignments/<str:crsId>',views.getCourseAssignments),
    path('getAllAssignments', views.getAllAssignments),
    path('createAssignment', views.createAssignment),
    path('updateAssignment', views.updateAssignment),
    path('deleteAssignment/<str:id>', views.deleteAssignment),

    path('login_user',views.login_user),
]