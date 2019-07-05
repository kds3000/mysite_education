from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from . import urls

class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        course_name = self.request.GET.get('course_name')
        if course_name:
            students = Student.objects.filter(courses__name=course_name)
        else:
            students = Student.objects.all()       
        return students      

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
            
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/add.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Student registration'
        print(context)
        return context
        
    def form_valid(self, form):
        response = super().form_valid(form)
        msg = 'Student %s %s has been successfully added' % (self.object.name, self.object.surname)
        messages.success(self.request, msg)
        return response
        
        
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/edit.html'
    
    def get_success_url(self):
        student_pk = self.kwargs['pk']
        return reverse_lazy('students:student_edit', kwargs={'pk':student_pk})
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Student info update'
        return context
        
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved')
        return response
        
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/remove.html'
    success_url = reverse_lazy('students:list_view')
    extra_context = {'title':'Student info suppression'}
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        msg = 'Student %s %s has been deleted' % (self.object.name, self.object.surname)
        messages.success(request, msg)
        return response
    
def list_view(request):
    course_name = request.GET.get('course_name')
    if course_name:
        students = Student.objects.filter(courses__name=course_name)
    else:
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
