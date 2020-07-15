from django import forms
from django.forms import ModelForm,Textarea
from .models import Funpost
class FunpostModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FunpostModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
    class Meta:
        model = Funpost
        exclude = ['user']