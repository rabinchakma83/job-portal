from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    display_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=User.USER_TYPE)
   
    class Meta:
        model = User
        fields = ['username', 'email', 'display_name', 'user_type', 'profile_picture', 'password1', 'password2']
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)          