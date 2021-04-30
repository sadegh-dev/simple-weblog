from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 30, widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter Username',
        }
    ))
    password = forms.CharField(max_length = 30, widget=forms.PasswordInput( 
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter password',
        }
    ))



class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length = 30, widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'your username',
        }
    ))
    email = forms.EmailField(max_length = 50, widget=forms.EmailInput( 
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'your email',
        }
    ))
    password = forms.CharField(max_length = 30, label='password' , widget=forms.PasswordInput( 
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'your password',
        }
    ))
    password2 = forms.CharField(max_length = 30, label='confirm password' , widget=forms.PasswordInput( 
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'your password',
        }
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email = email)
        if user.exists() :
            raise forms.ValidationError('this email Already exists.')
        return email

    def clean_password(self):
        p = self.cleaned_data['password']
        p2 = self.cleaned_data['password2']
        if p != p2 :

            raise forms.ValidationError('password is not match')
        return p

