from django.db import models
from django.urls import reverse
from .subquestions import Question



class RandomNumber(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    max_num = models.FloatField(null=True)
    min_num = models.FloatField(null=True)
    var_number = models.SmallIntegerField()
    integers_only = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('CreateAssignment-questions')
