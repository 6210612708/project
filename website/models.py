
from django.db import models
from django.utils import timezone
from .utils import file_path
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from annoying.fields import AutoOneToOneField
import datetime

# Create your models here.


class ListModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.list

# =====================================================


class CoorPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.list


class ComPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.list


class ProfPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.list


class StdPlanModel(models.Model):
    date = models.DateField(null=True)
    list = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to=file_path, null=True, blank=True)

    def __str__(self):
        return self.list

# =====================================================


class NewsModel(models.Model):
    title = models.CharField(max_length=500, null=True)
    detail = models.CharField(max_length=500, null=True)
    in_prof = models.BooleanField('in_prof', default=False)
    out_prof = models.BooleanField('out_prof', default=False)
    cn_std = models.BooleanField('cn_std', default=False)
    ee_std = models.BooleanField('ee_std', default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class DocModel(models.Model):
    title = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to=file_path, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# =====================================================

class ProfModel(models.Model):
    MAJOR = (
            ('ไฟฟ้า', 'ไฟฟ้า'),
            ('คอมพิวเตอร์', 'คอมพิวเตอร์'),
    )
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True, choices=MAJOR)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

# class OtherModel(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)
#     title = models.CharField(max_length=100, null=True)
#     fname = models.CharField(max_length=100, null=True)
#     lname = models.CharField(max_length=100, null=True)
#     email = models.EmailField(max_length=100, null=True)
#     phone = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return f'{self.fname} {self.lname}'


class StdModel(models.Model):
    MAJOR = (
            ('ไฟฟ้า', 'ไฟฟ้า'),
            ('คอมพิวเตอร์', 'คอมพิวเตอร์'),
    )
    TITLE = (
            ('นาย', 'นาย'),
            ('นางสาว', 'นางสาว'),
    )
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    stdid = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True, choices=TITLE)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True, choices=MAJOR)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class CoordinatorModel(models.Model):
    user = models.OneToOneField(
        ProfModel, null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.user}'


# ==================  PROJECT ===================================
class SubjectModel(models.Model):
    def current_year():
        return datetime.date.today().year + 543
    
    subject = models.CharField(max_length=200, null=True)
    year = models.IntegerField(null=True ,default=current_year)
    startterm = models.DateField(null=True)
    endterm = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.subject} {self.year}'

class ProjectModel(models.Model):
    STATUS = (
        ('ยังไม่มีนักศึกษาลงทะเบียน', 'ยังไม่มีนักศึกษาลงทะเบียน'),
        ('รอการอนุมัติ', 'รอการอนุมัติ'),
        ('อนุมัติ', 'อนุมัติ'),
    )
    thainame = models.CharField(max_length=100, null=True)
    engname = models.CharField(max_length=100, null=True)
    detail = models.CharField(max_length=500, null=True)
    consult = models.ForeignKey(
        ProfModel, on_delete=models.CASCADE, null=True, blank=True, related_name='consult')
    committee1 = models.ForeignKey(
        ProfModel, on_delete=models.CASCADE, null=True, blank=True, related_name='committee1')
    committee2 = models.ForeignKey(
        ProfModel, on_delete=models.CASCADE, null=True, blank=True, related_name='committee2')
    student1 = models.OneToOneField(
        StdModel, null=True, blank=True, on_delete=models.CASCADE, related_name='student1')
    student2 = models.OneToOneField(
        StdModel, null=True, blank=True, on_delete=models.CASCADE, related_name='student2')
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default='ยังไม่มีนักศึกษาลงทะเบียน')
    

    def __str__(self):
        return self.thainame

class Topicproject(models.Model):
    TOPIC = (
        ("proposal", "proposal"),
        ("preliminary", "preliminary"),
        ("progress1", "progress1"),
        ("progress2", "progress2"),
        ("draftthesis", "draftthesis"),
        ("finalthesis", "finalthesis"),
    )
    topic = models.CharField(max_length=200, null=True,choices=TOPIC)
    datedue = models.DateField(null=True)

    def __str__(self):
        return f'{self.topic} {self.datedue}'

class Fileproject(models.Model):
    project = models.ForeignKey(
        ProjectModel, on_delete=models.CASCADE, null=True,blank=True)
    topic = models.ForeignKey(
        Topicproject, on_delete=models.CASCADE, null=True,blank=True)
    file = models.FileField(upload_to=file_path, null=True ,blank=True,)
    date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.project} {self.topic}'


class ScoreConsult(models.Model):
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True, blank=True)
    std1 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std1con') 
    std2 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std2con')
    consult = models.ForeignKey(ProfModel, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, null=True, blank=True)
    sc1 = models.IntegerField(null=True, blank=True ,default=0)
    sc2 = models.IntegerField(null=True, blank=True ,default=0)
    sc3 = models.IntegerField(null=True, blank=True ,default=0)
    sc4 = models.IntegerField(null=True, blank=True ,default=0)
    sc5 = models.IntegerField(null=True, blank=True ,default=0)
    sc6 = models.IntegerField(null=True, blank=True ,default=0)
    sc7 = models.IntegerField(null=True, blank=True ,default=0)
    sc8 = models.IntegerField(null=True, blank=True ,default=0)
    score = models.IntegerField(null=True, blank=True ,default=0)
       
    def __str__(self):
        return f'{self.project} {self.subject}'

class ScoreCom1(models.Model):
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True, blank=True)
    std1 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std1sc1') 
    std2 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std2sc1')
    consult = models.ForeignKey(ProfModel, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, null=True, blank=True)
    sc1 = models.IntegerField(null=True, blank=True ,default=0)
    sc2 = models.IntegerField(null=True, blank=True ,default=0)
    sc3 = models.IntegerField(null=True, blank=True ,default=0)
    sc4 = models.IntegerField(null=True, blank=True ,default=0)
    sc5 = models.IntegerField(null=True, blank=True ,default=0)
    sc6 = models.IntegerField(null=True, blank=True ,default=0)
    sc7 = models.IntegerField(null=True, blank=True ,default=0)
    sc8 = models.IntegerField(null=True, blank=True ,default=0)
    score = models.IntegerField(null=True, blank=True ,default=0)
    
    def __str__(self):
        return f'{self.project} {self.subject}'

class ScoreCom2(models.Model):
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True, blank=True)
    std1 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std1sc2') 
    std2 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std2sc2')
    consult = models.ForeignKey(ProfModel, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, null=True, blank=True)
    sc1 = models.IntegerField(null=True, blank=True ,default=0)
    sc2 = models.IntegerField(null=True, blank=True ,default=0)
    sc3 = models.IntegerField(null=True, blank=True ,default=0)
    sc4 = models.IntegerField(null=True, blank=True ,default=0)
    sc5 = models.IntegerField(null=True, blank=True ,default=0)
    sc6 = models.IntegerField(null=True, blank=True ,default=0)
    sc7 = models.IntegerField(null=True, blank=True ,default=0)
    sc8 = models.IntegerField(null=True, blank=True ,default=0)
    score = models.IntegerField(null=True, blank=True ,default=0)
    
    def __str__(self):
        return f'{self.project} {self.subject}'

class ScoreModel(models.Model):
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, null=True, blank=True)
    std1 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std1') 
    std2 = models.OneToOneField(StdModel, null=True, on_delete=models.CASCADE, blank=True , related_name='std2')
    consult = models.ForeignKey(ProfModel, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, null=True, blank=True)
    consc = models.IntegerField(null=True, blank=True ,default=0)
    com1sc = models.IntegerField(null=True, blank=True ,default=0)
    com2sc = models.IntegerField(null=True, blank=True ,default=0)
    score = models.IntegerField(null=True, blank=True ,default=0)
    grade = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.project} {self.subject}'

class GradeModel(models.Model):
    subject = models.OneToOneField(SubjectModel, null=True, on_delete=models.CASCADE, blank=True ) 
    A = models.IntegerField(null=True)
    Bplus = models.IntegerField(null=True)
    B = models.IntegerField(null=True)
    Cplus = models.IntegerField(null=True)
    C = models.IntegerField(null=True)
    Dplus = models.IntegerField(null=True)
    D = models.IntegerField(null=True)
    F = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.subject}'
