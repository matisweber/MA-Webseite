from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField('Course Name', max_length= 120)
    teacher = models.CharField('Course Name Teacher', max_length= 60, null=True)
    email =models.EmailField('Teacher Email', max_length= 60, null=True, blank=True)
    language = models.CharField('Course Language', max_length= 60)
    languagelvl = models.CharField('Course level', max_length= 60)
    coursetype = models.CharField('Course Type', max_length= 60)
    info = models.TextField('Course Info', blank=True)


    def __str__(self):
        return self.name 
