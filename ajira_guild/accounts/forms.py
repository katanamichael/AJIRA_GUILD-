from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    username = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=User.USER_ROLES, required=True)
    region = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone', 'region', 'company_name', 'password']
