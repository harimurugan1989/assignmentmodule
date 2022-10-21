from django.db import models
from django.contrib.auth.models import User
from .create_link import CreateLink
from .question import Question


class Student(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    link=models.ForeignKey(CreateLink,on_delete=models.CASCADE)
    qno=models.ForeignKey(Question,on_delete=models.CASCADE)
