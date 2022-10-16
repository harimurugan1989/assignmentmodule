from xml.dom.pulldom import default_bufsize
from django.db import models
from django import forms
import random
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField, TextField, IntegerField
from django.urls import reverse
import os
import datetime
from django.conf import settings
# class quest(forms.Form):
#     question=forms.CharField()
#     answer=forms.CharField()

from pdf2image import convert_from_path, convert_from_bytes



class createlink(models.Model):
    link=models.CharField(max_length=12)
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    assignment_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50,blank=True )
    start = models.DateTimeField(blank=True, null=True)
    no_of_submissions= models.IntegerField(blank=True, null=True, default=0)
    perc_penalty= models.IntegerField(blank=True, default=0, null=True)
    first_sub_time = models.DateTimeField(blank=True, null=True)
    second_sub_time = models.DateTimeField(blank=True, null=True)
    notif= models.CharField(max_length=12)
    neg_mark=models.CharField(max_length=12)
    face_rec=models.CharField(max_length=12)
    res_anno=models.CharField(max_length=100)
    result_time = models.DateTimeField(blank=True, null=True)
    responses = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('CreateAssignment-home')

class instructions(models.Model):
     assignm= models.OneToOneField(createlink ,on_delete =models.CASCADE)
     instruction = models.TextField()

     def get_absolute_url(self):
         return reverse('CreateAssignment-instructions')


class questiondata(models.Model):

    # level = models.CharField(max_length=5)
    # time = models.IntegerField()
    des1 = models.TextField(blank=True)
    # des2 = models.TextField(blank=True)
    # des3 = models.TextField(blank=True)
    # des4 = models.TextField(blank=True)
    # des5 = models.TextField(blank=True)
    # # options = models.TextField()
    photo1 = models.ImageField(blank=True,  null=True ,upload_to = 'ques_img')
    # photo2 = models.ImageField(blank=True,  null=True ,upload_to = 'ques_img')
    # photo3 = models.ImageField(blank=True,  null=True ,upload_to = 'ques_img')
    # photo4 = models.ImageField(blank=True,  null=True ,upload_to = 'ques_img')
    # photo5 = models.ImageField(blank=True,  null=True ,upload_to = 'ques_img')
    rmin1=models.IntegerField(default=1, blank=True)
    rmax1=models.IntegerField(default=100, blank=True)
    rmin2=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)
    rmax2=models.IntegerField(default=0, null=True, blank=True)
    rmin3=models.IntegerField(default=0, null=True, blank=True)
    rmax3=models.IntegerField(default=100, null=True, blank=True)
    mark1=models.IntegerField(default=1, null=True, blank=True)
    ques1=models.TextField(blank=True, null= True)
    ans1=models.TextField(blank=True, null=True)
    exp1=models.TextField(blank=True, null=True)
    # mark2=models.IntegerField(default=1, null=True)
    # ques2=models.TextField(blank=True, null= True)
    # ans2=models.TextField(blank=True, null=True)
    # exp2=models.TextField(blank=True, null=True)
 
    # mark3=models.IntegerField(default=1, null=True)
    # ques3=models.TextField(blank=True, null= True)
    # ans3=models.TextField(blank=True, null=True)
    # exp3=models.TextField(blank=True, null=True)
 
    # mark4=models.IntegerField(default=1, null=True)
    # ques4=models.TextField(blank=True, null= True)
    # ans4=models.TextField(blank=True, null=True)
    # exp4=models.TextField(blank=True, null=True)
 
    # mark5=models.IntegerField(default=1, null=True)
    # ques5=models.TextField(blank=True, null= True)
    # ans5=models.TextField(blank=True, null=True)
    # exp5=models.TextField(blank=True, null=True)
 
    # rmin4=models.IntegerField(default=1, null=True)
    # rmax4=models.IntegerField(default=100, null=True)
    # rmin5=models.IntegerField(default=1, null=True)
    # rmax5=models.IntegerField(default=100, null=True)
    # # qno = models.IntegerField(null=True)
    
    link=models.ForeignKey(createlink,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('CreateAssignment-addquestion')


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no=models.TextField()
    college=models.TextField()
    # avatar = models.CharField(max_length=2)
    type=models.CharField(max_length=15)
    # def __str__(self):
    #     return f'{self.user.username} Profile'
        
    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('createquiz-home')

class st_data(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    link = models.ForeignKey(createlink,on_delete=models.CASCADE)
    answer = models.TextField()

