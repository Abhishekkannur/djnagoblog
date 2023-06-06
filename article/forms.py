from django.contrib.auth.models import User
from .models import *
from django import forms

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','first_name','email')
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passowrd is not matching')
        return cd['password2']
    
class ArticleAddingForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= ('title','discription')
class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= ('title','discription')
    
