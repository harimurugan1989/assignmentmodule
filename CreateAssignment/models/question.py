from django.db import models
from django.urls import reverse
from .create_link import CreateLink



class Question(models.Model):
    assignment = models.ForeignKey(CreateLink,on_delete=models.CASCADE)
    order = models.TextField(default = '[]')

    def get_absolute_url(self):
        return reverse('CreateAssignment-questions')
