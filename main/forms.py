from django import forms
from django.forms import models
from django.forms import ModelForm

from .models import Worker, Department, Language


class AddWorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'age', 'sex', 'department', 'language']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'language': forms.Select(attrs={'class': 'form-select'})
        }


class AddDepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'floor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'})
        }


class AddLanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
