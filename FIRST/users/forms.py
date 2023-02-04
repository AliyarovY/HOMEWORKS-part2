from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'country', 'avatar',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email',)


class PassRecForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)





