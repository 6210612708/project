
from django.db import models

# Create your models here.


class ListModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)