from django.db import models
from django.contrib.auth.models import User
from .create_link import CreateLink
from .question import Question
from .subquestions import SubQuestion


class StudentScore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    link = models.ForeignKey(CreateLink,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)