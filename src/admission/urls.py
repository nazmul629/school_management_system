from django.urls import path
from .views import *

urlpatterns = [
    path('student_admission/',admission_student, name = "admission_student"),
    path('classes/',class_list,name = "classes"),
    path('students/<Class>/',student_list,name = "student_list"),
    path('student/details/<int:id>',student_details, name = "student_details"),
    path('studentinfo/edit/<int:id>',studentinfo_edit, name = "studentinfo_edit"),
    path('student/delet/<int:id>',studentinfo_delete, name = "studentinfo_delete")

    

]