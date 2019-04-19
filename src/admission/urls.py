from django.urls import path
from .views import *

urlpatterns = [
    path('student_admission/',admission_student, name="admission_student"),
    path('classes/',class_list,name="classes"),
    path('students/<Class>/',student_list,name="student_list")
    

]