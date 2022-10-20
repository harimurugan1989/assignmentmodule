from os import link
from django.db import models
import random
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField, TextField
from django.urls import reverse
    
class createlink(models.Model):
    link=models.CharField(max_length=12)
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    assignment_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    start = models.DateTimeField()
    no_of_submissions= models.IntegerField()
    perc_penalty= models.IntegerField()
    first_sub_time = models.DateTimeField()
    extend = models.CharField(max_length=5)
    second_sub_time = models.DateTimeField()
    notif= models.CharField(max_length=12)
    neg_mark=models.CharField(max_length=12)
    face_rec=models.CharField(max_length=12)
    res_anno=models.CharField(max_length=100)
    result_time = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('CreateAssignment-home')


class Instruction(models.Model):
    assignment = models.OneToOneField(createlink,on_delete =models.CASCADE)
    instructions = models.TextField(max_length=500, blank= True)

    def get_absolute_url(self):
        return reverse('CreateAssignment-instructions')

class Question(models.Model):
    assignment = models.ForeignKey(createlink,on_delete=models.CASCADE)
    question= models.TextField(max_length=100, blank= True)
    rand_variable_min=models.IntegerField()
    rand_variable_max=models.IntegerField()
    explanation=models.TextField(max_length=300, blank= True)

    def get_absolute_url(self):
        return reverse('CreateAssignment-questions')

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no=models.CharField(max_length=20)
    college=models.TextField()
    type=models.CharField(max_length=15)
    def __str__(self):
        return f'{self.user.username} Profile'

class Student(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    link=models.ForeignKey(createlink,on_delete=models.CASCADE)
    qno=models.ForeignKey(Question,on_delete=models.CASCADE)
    R=models.JSONField()
    
    
