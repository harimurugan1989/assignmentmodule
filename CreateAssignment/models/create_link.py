from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
    
class CreateLink(models.Model):
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
