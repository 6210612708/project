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

