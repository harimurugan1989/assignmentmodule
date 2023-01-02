from django.db import models
from django.urls import reverse
from .create_link import CreateLink
from .question import Question



class SubQuestion(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    text = models.TextField()
    answer = models.TextField()
    explanation = models.TextField()
    score = models.IntegerField(default=1)
    tollerance = models.FloatField(default=2)