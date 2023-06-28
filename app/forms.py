from django import forms

class Topic(forms.Form):
    Topic_names=forms.CharField(max_length=100)
    
class Webpage(forms.Form):
    Topic_names=forms.InlineForeignKeyField(Topic)
    Name=forms.CharField(max_length=10)
    Url =forms.URLField(max_length=100)