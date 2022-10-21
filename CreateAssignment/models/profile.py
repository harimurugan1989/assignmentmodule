from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no=models.CharField(max_length=20)
    college=models.TextField()
    type=models.CharField(max_length=15)
    def __str__(self):
        return f'{self.user.username} Profile'
