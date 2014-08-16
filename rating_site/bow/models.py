from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=50,null=True,blank=True)

class Restaurant(models.Model):
	res_name = models.CharField(max_length=200)
	location = models.CharField(max_length=100,null=True,blank=True)


class UserBW(models.Model):
      user = models.CharField(max_length=100)
      btr_res = models.ForeignKey(Restaurant,related_name="btr")
      wrs_res = models.ForeignKey(Restaurant,related_name="wrs")


class UserBW2(models.Model):
      user = models.CharField(max_length=100)
      btr_res = models.CharField(max_length=100)
      wrs_res = models.CharField(max_length=100)
