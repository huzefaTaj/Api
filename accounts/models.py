import email
from email.policy import default
from sre_parse import State
from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.CharField(max_length = 200, default='' ,blank=True)
    email=models.CharField(max_length = 200,default='' ,blank=True)
    location = models.CharField(max_length = 200,default='', blank=True)
    state = models.CharField(max_length = 200,default='',blank=True )
    gender = models.CharField(max_length = 200,default='',blank=True )