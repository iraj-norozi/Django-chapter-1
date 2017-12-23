from django.shortcuts import render,HttpResponse
from .models import Student
from .forms import StudentForm

def hello(request):
    #form = StudentForm()
    if request.method=="POST":
        form = StudentForm(data=request.POST)

        if form.is_valid():
            form.save()

    students = Student.objects.all()
    forms = StudentForm()
    return render(request, 'index.html', {"Title":"index","students":students, "forms":forms})

def show(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request,'show.html',{"Title":"SHOW","student": student })
