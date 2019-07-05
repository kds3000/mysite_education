from django.db import models
from coaches.models import Coach
from django.urls import reverse_lazy

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    coach = models.ForeignKey(Coach, models.CASCADE, related_name='coach_courses', null='True', blank='True')
    assistant = models.ForeignKey(Coach, models.CASCADE, related_name='assistant_courses', null='True', blank='True')
    
    def __str__(self):
        return self.name
        
        
class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, models.CASCADE)
    order = models.PositiveIntegerField()
    
    def get_absolute_url(self):
        course_id = self.course_id
        course = Course.objects.get(id=course_id)
        return reverse_lazy('courses:detail', kwargs={'course_name':course.name,})
    
    def __str__(self):
        return self.subject