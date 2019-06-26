from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return self.name
        
        
class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, models.CASCADE)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return self.subject