from django import forms


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

