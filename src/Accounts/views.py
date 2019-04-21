from django.shortcuts import render,redirect
from admission.models import StudentInfo
from .forms import Add_month_form
from . models import Select_Month

def select_fees_month(request):
    if request.method == "POST":
        form = Add_month_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_fees")    
    form = Add_month_form()
    context = {"forms":form}
    return render(request,"accounts/select_month.html",context)

def add_student_fees(request):
    month = Select_Month.objects.all()
    all_student = StudentInfo.objects.all()
    context = {"all_student":all_student}
    return render(request,"accounts/add_fees.html",context)



