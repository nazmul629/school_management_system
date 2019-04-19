from django.shortcuts import render
from .models import Schoolinfo

def schoolinfo(request):
    schoolinfo = Schoolinfo.objects.all()
    context = {
        "schoolinfo":schoolinfo
    }
    return render(request, 'home.html',context)