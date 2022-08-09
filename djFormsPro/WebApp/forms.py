from django import forms
class EmpForms(forms.Form):
    Name=forms.CharField()
    Job=forms.CharField()
    Loc=forms.CharField()
    Sal=forms.FloatField()