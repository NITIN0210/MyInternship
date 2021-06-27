from django.db import models

# Create your models here.
class UserData(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	email=models.EmailField(max_length=30)
	mobile=models.IntegerField()
	gender=models.CharField(max_length=10)
	pswd=models.CharField(max_length=30)