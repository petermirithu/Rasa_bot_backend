from django.urls import re_path, path
from api import views

urlpatterns=[    
    path('getOneStudent/<str:id>', views.getOneStudent),
    path('getAllStudents', views.getAllStudents),
    path('createStudent', views.createStudent),
    path('updateStudent', views.updateStudent),
    path('deleteStudent/<str:id>', views.deleteStudent),
    
    path('getOneCourse/<str:id>', views.getOneCourse),
    path('getAllCourses', views.getAllCourses),
    path('createCourse', views.createCourse),
    path('updateCourse', views.updateCourse),
    path('deleteCourse/<str:id>', views.deleteCourse),
    
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