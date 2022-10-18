from django.urls import re_path
from api import views

urlpatterns=[
    re_path(r'^student$', views.studentApi),
    re_path(r'^student/([0-9]+)$', views.studentApi),
    re_path(r'^course$', views.courseApi),
    re_path(r'^course/([0-9]+)$', views.courseApi),
    re_path(r'^faculty$', views.facultyApi),
    re_path(r'^faculty/([0-9]+)$', views.facultyApi),
    re_path(r'^assignment$', views.assignmentApi),
    re_path(r'^assignment/([0-9]+)$', views.assignmentApi)
]