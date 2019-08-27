from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

'''
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    yrsold = models.DecimalField(max_digits=3, decimal_places=0)
    skills = models.CharField(max_length=50, blank=True)
'''
'''
class UserManager(BaseUserManager):
    def create_user(username, realname, useremail, password):
'''

class Account(models.Model):
    username = models.CharField(max_length=12)
    realname = models.CharField(max_length=4)
    useremail = models.EmailField()
    password = models.SlugField(max_length=15)
