from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import *

class ListModelForm(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }

class CoorPlanModelForm(forms.ModelForm):
    class Meta:
        model = CoorPlanModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }

class ComPlanModelForm(forms.ModelForm):
    class Meta:
        model = ComPlanModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }

class ProfPlanModelForm(forms.ModelForm):
    class Meta:
        model = ProfPlanModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }

class StdPlanModelForm(forms.ModelForm):
    class Meta:
        model = StdPlanModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }
   

class NewsModelForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = "__all__"
        exclude = ['date_created']


class DocModelForm(forms.ModelForm):
    class Meta:
        model = DocModel
        fields = "__all__"
        exclude = ['date_created']


class ProfModelForm(forms.ModelForm):
    class Meta:
        model = ProfModel
        fields = "__all__"


class OtherModelForm(forms.ModelForm):
    class Meta:
        model = OtherModel
        fields = "__all__"


class StdModelForm(forms.ModelForm):
    class Meta:
        model = StdModel
        fields = "__all__"


class projectModelForm(forms.ModelForm):
    consult = forms.CharField(widget=forms.HiddenInput(), initial="123") 
    class Meta:
        model = ProjectModel
        fields = "__all__"
        exclude = ['student1' ,'student2' ,'committee' ,'status']

class projectForm(forms.Form):
    thainame = forms.CharField(max_length=100)
    engname = forms.CharField(max_length=100)
    detail = forms.CharField(max_length=500)





