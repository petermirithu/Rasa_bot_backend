from django.urls import re_path
from api import views

urlpatterns=[
    re_path(r'^student$', views.studentApi),
    re_path(r'^student/([0-9]+)$', views.studentApi)
]