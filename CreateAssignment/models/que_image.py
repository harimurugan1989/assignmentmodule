from django.db import models
from .question import Question


class QueImg(models.Model):
    image = models.ImageField(upload_to = 'que_desc_images/')
    question = models.ForeignKey(Question,on_delete= models.CASCADE)