from django.db import models
from django.urls import reverse
from CreateAssignment.models import CreateLink


class Instruction(models.Model):
    assignment = models.OneToOneField(CreateLink,on_delete =models.CASCADE)
    instructions = models.TextField(max_length=500, blank= True)

    def get_absolute_url(self):
        return reverse('CreateAssignment-instructions')
