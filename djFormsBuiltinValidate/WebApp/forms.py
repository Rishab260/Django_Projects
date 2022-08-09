from django import forms
from django.core import validators

class EmpForm(forms.Form):
    Name=forms.CharField()
    Salary=forms.IntegerField()
    BotField=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print("Welcome to Bot Validations..!!")
        cdata=super().clean()
        bhan=cdata['BotField']
        if len(bhan)>0:
            raise forms.ValidationError("Sorry UR a BOT...!!")
