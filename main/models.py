from django.db import models
import uuid
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    unit = models.IntegerField(default=0)
    imgUrl = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    