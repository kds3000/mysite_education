from django.shortcuts import render

from .models import Student

    
def list_view(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, '../templates/students/list.html', context)
  
def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student':student
    }
    return render(request, '../templates/students/detail.html', context)


