from django.db import models
from django.contrib.auth.models import AbstractUser

class myuser(AbstractUser):
    level = models.IntegerField(default=0)