
from django.db import models
from django.utils import timezone
from .utils import file_path
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from annoying.fields import AutoOneToOneField

# Create your models here.


class ListModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.list
    
# =====================================================

class CoorPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.list

class ComPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.list

class ProfPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.list

class StdPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=64, null=True)
    file = models.FileField(upload_to=file_path,null=True,blank=True)
    
    def __str__(self):
        return self.list

# =====================================================

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
    

# =====================================================

class ProfModel(models.Model):
    MAJOR = (
            ('ไฟฟ้า', 'ไฟฟ้า'),
            ('คอมพิวเตอร์', 'คอมพิวเตอร์'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True, choices=MAJOR)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.fname} {self.lname}'

class OtherModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.fname} {self.lname}'

class StdModel(models.Model):
    MAJOR = (
            ('ไฟฟ้า', 'ไฟฟ้า'),
            ('คอมพิวเตอร์', 'คอมพิวเตอร์'),
    )
    TITLE = (
            ('นาย', 'นาย'),
            ('นางสาว', 'นางสาว'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)
    stdid = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True, choices=TITLE)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True, choices=MAJOR)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.fname} {self.lname}'
<<<<<<< HEAD

# =====================================================
=======
    

class CoordinatorModel(models.Model):
    user = models.OneToOneField(ProfModel, null=True, on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return f'{self.user}'


# ==================  PROJECT ===================================


class ProjectModel(models.Model):
    STATUS = (
            ('ยังไม่มีนักศึกษาลงทะเบียน', 'ยังไม่มีนักศึกษาลงทะเบียน'),
            ('รอการอนุมัติ', 'รอการอนุมัติ'),
            ('อนุมัติ', 'อนุมัติ'),
    )
    thainame = models.CharField(max_length=100, null=True)
    engname = models.CharField(max_length=100, null=True)
    detail = models.CharField(max_length=500, null=True)
    consult = models.ForeignKey(ProfModel, on_delete=models.CASCADE , null=True ,blank=True)
    committee = models.CharField(max_length=100, null=True , blank=True)
    student1 = models.OneToOneField(StdModel, null=True, blank=True, on_delete=models.CASCADE , related_name='student1')
    student2 = models.OneToOneField(StdModel, null=True, blank=True, on_delete=models.CASCADE , related_name='student2')
    status = models.CharField(max_length=200, null = True, choices=STATUS, default='ยังไม่มีนักศึกษาลงทะเบียน')
    

    def __str__(self):
        return self.thainame
    
class Docproject(models.Model):
    project = AutoOneToOneField(ProjectModel,on_delete=models.CASCADE ,primary_key=True)
    proposal = models.FileField(upload_to=file_path,null=True,blank=True)
    preliminary = models.FileField(upload_to=file_path,null=True,blank=True)
    progress1 = models.FileField(upload_to=file_path,null=True,blank=True)
    progress2 = models.FileField(upload_to=file_path,null=True,blank=True)
    draftthesis = models.FileField(upload_to=file_path,null=True,blank=True)
    finalthesis = models.FileField(upload_to=file_path,null=True,blank=True)
    
    
class GradeModel(models.Model):
    A = models.IntegerField(null=True)
    Bplus = models.IntegerField(null=True)
    B = models.IntegerField(null=True)
    Cplus = models.IntegerField(null=True)
    C = models.IntegerField(null=True)
    Dplus = models.IntegerField(null=True)
    D = models.IntegerField(null=True)
    F = models.IntegerField(null=True)
>>>>>>> a1fb504be64f889b67acc570852c566e999ac4c9
