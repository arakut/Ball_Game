from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.CharField(label='Электронная почта', widget=forms.EmailInput(attrs={'calss': 'form-input'}))
    username = forms.CharField(label='Ник пользователя', widget=forms.TextInput(attrs={'calss': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'calss': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'calss': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Имя')
    age = forms.IntegerField(label='Возраст')
    image = forms.ImageField(label='Фото пользователя')
    social_urls = forms.CharField(label='Ссылки на социальные сети')

    class Meta:
        model = Profile
        fields = ['name', 'image', 'age', 'social_urls']
