from django.urls import path
from .views import auth_form

urlpatterns = [
    path('', auth_form)
]
