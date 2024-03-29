from django.shortcuts import render, redirect
from .models import Lesson, Course
from students.models import Student
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView
    
def detail(request, course_name):
    lessons = Lesson.objects.filter(course__name=course_name)
    course = Course.objects.get(name=course_name)
    context = {
        'lessons':lessons,
        'course':course,
    }
    return render(request, '../templates/courses/detail.html', context)
    
def course_add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            msg = 'Course ' + form.cleaned_data['name'] + ' has been successfully added'
            messages.success(request, msg)
            return redirect('index')            
    else:
        form = CourseModelForm()
    return render(request, '../templates/courses/add.html', {'form':form})
    
def course_edit(request, course_name):
    course = Course.objects.get(name=course_name)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            instance = form.save()
            msg = 'The changes have been saved'
            messages.success(request, msg)            
    else:
        form = CourseModelForm(instance=course)
    return render(request, '../templates/courses/edit.html', {'form':form})
    
def course_remove(request, course_name):
    course = Course.objects.get(name=course_name)
    if request.method == 'POST':
        msg = 'Course ' + course.name + ' has been deleted'
        instance = course.delete()
        messages.success(request, msg)
        return redirect('index')            
    return render(request, '../templates/courses/remove.html', {'course':course})
    
class SuccessMessageMixin():
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Lesson %s has been successfully added' % self.object.subject)
        return response    
    
class LessonCreateView(SuccessMessageMixin, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    form_class = LessonModelForm
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Создание нового урока'
        return context
        

'''    
def add_lesson(request, course_name):
    course = Course.objects.get(name=course_name)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            msg = 'Lesson ' + form.cleaned_data['subject'] + ' has been successfully added'
            messages.success(request, msg)
            return redirect(reverse('courses:detail', args=(course_name,)))            
    else:
        form = LessonModelForm(initial = {'course':course})
    return render(request, '../templates/courses/add_lesson.html', {'form':form})    
'''
