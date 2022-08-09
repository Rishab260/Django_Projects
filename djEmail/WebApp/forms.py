from django import forms
class SentForm(forms.Form):
    name=forms.CharField(max_length=100)
    mail=forms.CharField(max_length=100)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(required=False)