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
    list = forms.CharField(max_length=160)

class ListModelForm(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
        }

