from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import *


class todoForm(forms.Form):
    date = forms.DateField(widget=AdminDateWidget())
    list = forms.CharField(max_length=64)

class ListModelForm(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }


class newsForm(forms.Form):
    title = forms.CharField(max_length=160)
    detail = forms.CharField(max_length=160)


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = "__all__"
        exclude = ['date_created']
