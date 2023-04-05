from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
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
        exclude = ['user']


# class OtherModelForm(forms.ModelForm):
#     class Meta:
#         model = OtherModel
#         fields = "__all__"
#         exclude = ['user']


class StdModelForm(forms.ModelForm):
    class Meta:
        model = StdModel
        fields = "__all__"
        exclude = ['user']


class projectModelForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = "__all__"
        exclude = ['student1', 'student2', 'committee', 'status', 'consult']

# class projectForm(forms.Form):
#     thainame = forms.CharField(max_length=100)
#     engname = forms.CharField(max_length=100)
#     detail = forms.CharField(max_length=500)


class applyprojectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['student1', 'student2']


class coordinatorForm(forms.ModelForm):
    class Meta:
        model = CoordinatorModel
        fields = "__all__"
        
class fileprojectForm(forms.ModelForm):
    class Meta:
        model = Fileproject
        fields = "__all__"
        exclude = ['date']


class docprojectForm(forms.Form):
    SELECT_FOR_TERM_ONE = (
        ("proposal", "proposal"),
        ("preliminary", "preliminary"),
        ("progress1", "progress1"),
    )
    SELECT_FOR_TERM_TWO = (
        ("progress2", "progress2"),
        ("draftthesis", "draftthesis"),
        ("finalthesis", "finalthesis"),

    )
    trem1 = forms.TypedChoiceField(choices=SELECT_FOR_TERM_ONE, coerce=str)
    trem2 = forms.ChoiceField(choices=SELECT_FOR_TERM_TWO)
    file = forms.FileField()
    date = forms.DateTimeField(widget=forms.HiddenInput())


class GradeForm(forms.ModelForm):
    class Meta:
        model = GradeModel
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectModel
        fields = "__all__"
        widgets = {
            "startterm": AdminDateWidget(),
            "endterm": AdminDateWidget(),
        }
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = ScoreModel
        fields = "__all__"
        exclude = ['subject', 'std1', 'std2', 'consult', 'project']


