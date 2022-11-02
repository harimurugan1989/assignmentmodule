from django.db import models
from django.urls import reverse
from .subquestions import SubQuestion



class RandomNumber(models.Model):
    subquestion = models.ForeignKey(SubQuestion,on_delete = models.CASCADE)
    max = models.BigIntegerField()
    min = models.BigIntegerField()
    var_number = models.SmallIntegerField()
    
    def get_absolute_url(self):
        return reverse('CreateAssignment-questions')
