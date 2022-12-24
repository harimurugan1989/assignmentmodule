from django.db import models
from .question import Question


class QueText(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question,on_delete= models.CASCADE)
    