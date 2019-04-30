from django.db import models
from django.forms.widgets import Textarea
from astropy.table.operations import unique


class User(models.Model):
    userName=models.CharField(max_length=200,unique=True)
    userPassword=models.CharField(max_length=200)
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    address=models.TextField(blank=True,null=True)

class UserLogin(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    loginStatus=models.BooleanField(default=False)

# Create your models here.
