
from django.db import models
from django.utils import timezone

# Create your models here.


class ListModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.list

class NewsModel(models.Model):
    title = models.CharField(max_length=64, null=True)
    detail = models.CharField(max_length=500, null=True)
    in_prof = models.BooleanField('in_prof', default=False)
    out_prof = models.BooleanField('out_prof', default=False)
    cn_std = models.BooleanField('cn_std', default=False)
    ee_std = models.BooleanField('ee_std', default=False)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

