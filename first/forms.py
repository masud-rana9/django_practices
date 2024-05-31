from django import forms
from django.core import validators
class DjangoForm(forms.Form):
    mobile = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    laptop = forms.CharField( required=False)
  


    
        