from django.shortcuts import render,redirect
from .models import StudentInfo,Schoolallclass
from .forms import AdmissionStudentForm

def class_list(request):
        all_class = Schoolallclass.objects.all()
        context ={'all_class':all_class} 
        return render(request,'studentinfo/class_list.html',context)

def student_list(request,Class):
        student_list = StudentInfo.objects.filter(Class__Class=Class)
        context = {'student_list':student_list}
        print(student_list)
        return render(request,'studentinfo/student_list.html',context)



def admission_student(request):
    if request.method == "POST":
        form = AdmissionStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    form = AdmissionStudentForm()
    context = {"forms":form}
    return render(request,'studentinfo/admissionstudent.html',context)
