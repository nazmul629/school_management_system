from django.shortcuts import render,redirect
from .models import StudentInfo,Schoolallclass
from .forms import AdmissionStudentForm

def class_list(request):
        all_class = Schoolallclass.objects.all()
        context ={'all_class':all_class} 
        return render(request,'studentinfo/class_list.html',context)

def admission_student(request):
    if request.method == "POST":
        form = AdmissionStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    form = AdmissionStudentForm()
    context = {"forms":form}
    return render(request,'studentinfo/admissionstudent.html',context)


def student_list(request,Class):
        student_list = StudentInfo.objects.filter(Class__Class=Class)
        context = {'student_list':student_list}
        return render(request,'studentinfo/student_list.html',context)


def student_details(request,id):
        student = StudentInfo.objects.get(id=id)
        context={'student':student}
        print(student)
        return render(request,'studentinfo/student_details.html',context)

def studentinfo_edit(request,id):
        select = StudentInfo.objects.get(id=id)
        form = AdmissionStudentForm(request.POST or None, instance=select)
        if request.method=='POST':
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                        return redirect('student_details', id=post.id)
        context = {'form':form,
                    "student":select       }
        return render(request,'studentinfo/studentinfo_edit.html',context)

def studentinfo_delete(request,id):
        select = StudentInfo.objects.get(id=id)
        select.delete()
        return redirect("classes")