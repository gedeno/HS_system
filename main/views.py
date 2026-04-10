from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/login/'
