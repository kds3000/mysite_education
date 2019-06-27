from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=50)
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
    
    def __str__(self):
        return self.subject