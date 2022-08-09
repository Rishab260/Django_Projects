from django import forms
class EmpForm(forms.Form):
    Name=forms.CharField()
    Job=forms.CharField()
    Loc=forms.CharField()
    Sal=forms.FloatField()