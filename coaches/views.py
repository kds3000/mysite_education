from django.shortcuts import render
from .models import Coach
from courses.models import Course

def detail(request, coach_name):
    coach_splitted = coach_name.split()
    coach = Coach.objects.get(user__first_name=coach_splitted[0], user__last_name=coach_splitted[1])
    #courses = Course.objects.filter(coach__user__first_name=coach_splitted[0], coach__user__last_name=coach_splitted[1])
    coach_courses = coach.coach_courses.all()
    assistant_courses = coach.assistant_courses.all()
    context = {
        'coach':coach,
        'coach_courses':coach_courses,
        'assistant_courses':assistant_courses
    }
    return render(request, '../templates/coaches/detail.html', context)
