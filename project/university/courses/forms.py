from django import forms
from .models import *

class SpecialForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.SlugField(max_length=512)
    start_date = forms.DateField()
    is_active = forms.BooleanField()

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'degree']



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'specialities','teachers']