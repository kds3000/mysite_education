from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages
    
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

def student_add(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            msg = 'Student ' + form.cleaned_data['name'] + ' ' + form.cleaned_data['surname'] + ' has been successfully added'
            messages.success(request, msg)
            return redirect('index')            
    else:
        form = StudentModelForm()
    return render(request, '../templates/students/add.html', {'form':form})
    
def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            instance = form.save()
            msg = 'The changes have been saved'
            messages.success(request, msg)            
    else:
        form = StudentModelForm(instance=student)
    return render(request, '../templates/students/edit.html', {'form':form})
    
def student_remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        msg = 'Student ' + student.name + ' ' + student.surname + ' has been deleted'
        instance = student.delete()
        messages.success(request, msg)
        return redirect('index')            
    return render(request, '../templates/students/remove.html', {'student':student})
