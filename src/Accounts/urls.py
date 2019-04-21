from django.urls import path
from . views import *

urlpatterns = [
    path("select_month/",select_fees_month,name="select_month"),
    path("add_student_fees/",add_student_fees, name="add_fees"),

]