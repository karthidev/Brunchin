from django.db import models
from django import forms
from django.contrib.auth.models import User


class Brunchin_Food(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class user_login(models.Model):
 firstname = models.CharField(max_length=255)
 lastname = models.CharField(max_length=255)
 password = models.CharField(max_length=255)

class foot_category(models.Model):
    food_name=models.CharField(max_length=255)
    food_type=models.CharField(max_length=255)
    food_restaurant=models.CharField(max_length=255)
    food_price=models.CharField(max_length=255)
    food_img= models.ImageField(upload_to='images')  

class brunch_cart(models.Model):
    userid=models.IntegerField()
    product_id=models.IntegerField()
    fo_name=models.CharField(max_length=255)
    fo_type=models.CharField(max_length=255)
    fo_price=models.IntegerField()
    fo_img= models.ImageField(upload_to='images')  