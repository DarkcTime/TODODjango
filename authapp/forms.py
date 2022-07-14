from django import forms

class auth_app_form(forms.Form):
    Login = forms.CharField(max_length=100, label='Логин')
    Password = forms.CharField(max_length=100, label='Пароль')