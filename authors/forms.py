from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        
        labels  = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'password': 'password',
        }
        
        help_texts = {
            'Email': 'The e-mail be must valid',
        }
        
        error_messages = {
            'username' : {
                'required': 'This field must not be empty',
                'max_length': 'This field must have  less then 65 characters'
            }
        }
        
        widgets = {
            'username': forms.TextInput(attrs=
                        {
                            'class': 'form-control', 'placeholder': 'Username'
                        }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here'
            })
        }
