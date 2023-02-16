
from django.db import models
from django.utils import timezone
from .utils import file_path

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

class DocModel(models.Model):
    title = models.CharField(max_length=64, null=True)
    file = models.FileField(upload_to=file_path,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class ProfModel(models.Model):
    MAJOR = (
            ('ไฟฟ้า', 'ไฟฟ้า'),
            ('คอมพิวเตอร์', 'คอมพิวเตอร์'),
    )

    title = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True, choices=MAJOR)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.fname} {self.lname}'