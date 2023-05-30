from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=32)
    height = models.IntegerField()
    weight = models.IntegerField(default=100)
    age = models.IntegerField()