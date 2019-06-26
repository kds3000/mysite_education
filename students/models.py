from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    skype = models.CharField(max_length=30, null=True, blank=True)
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.surname + ' ' + self.name
        
    def get_courses(self):
        return self.courses.all()