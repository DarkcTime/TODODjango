from django import forms

class auth_app_form(forms.Form):
    Login = forms.CharField(max_length=100, label='Логин или email')
    Password = forms.CharField(max_length=100, label='Пароль')
    RememberMe = forms.BooleanField(label='Запомнить меня')