from django import forms
class StdForm(forms.Form):
    SName=forms.CharField()
    SFee=forms.IntegerField()
    SLoc = forms.CharField()
    SRes = forms.CharField()
    SGrd = forms.CharField()