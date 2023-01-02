from django.db import models
from django.contrib.auth.models import User
from .create_link import CreateLink
from .question import Question
from .subquestions import SubQuestion


class StudentRandom(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    randoms = models.TextField()
