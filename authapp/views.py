from django.shortcuts import render
from .forms import auth_app_form 

TITLE_AUTH_FORM = "Авторизация"

# Create your views here.
# form for auth in project
def auth_form(request):
    auth_form = auth_app_form() 
    return render(request, 'authapp/authapp.html', 
    {   'title': TITLE_AUTH_FORM,
        'form': auth_form})