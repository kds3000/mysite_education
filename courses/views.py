from django.shortcuts import render

from .models import Lesson, Course
from students.models import Student

    
def detail(request, course_name):
    lessons = Lesson.objects.filter(course__name=course_name)
    course = Course.objects.get(name=course_name)
    context = {
        'lessons':lessons,
        'course':course
    }
    return render(request, '../templates/courses/detail.html', context)
    
def list_view_for_course(request, course_name):
    students = Student.objects.filter(courses__name=course_name)
    context = {
        'students':students
    }
    return render(request, '../templates/students/list.html', context)


