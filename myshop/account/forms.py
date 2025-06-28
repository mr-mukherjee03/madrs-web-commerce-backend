from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput, label='Password')

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput, label='Password')
    password2=forms.CharField(widget=forms.PasswordInput, label='Repeat Password')

    class Meta:
        model=get_user_model()
        fields=['username','first_name', 'email']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        data=self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already exists.')
        return data