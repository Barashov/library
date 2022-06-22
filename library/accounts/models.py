from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    reqistration_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30)
    
    
    

