from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('m', 'Male'),('f', 'Female')))
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
        
   
        