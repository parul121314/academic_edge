from django.db import models
from distutils.command.upload import upload

class loginac(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
