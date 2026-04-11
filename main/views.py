from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView ,TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Personal, Contact_address, Emergency_contact, Course, Assessment
from .forms import PersonalForm, ContactAddressForm, EmergencyContactForm, CourseForm, AssessmentForm

# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = '/logins/'

class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = '/home/'
@method_decorator(login_required(login_url='/logins/'), name='dispatch')
class HomeView(TemplateView):
    template_name = 'main/home.html'

class PersonalView(CreateView):
    form_class = PersonalForm
    template_name = 'main/personal.html'
    success_url = '/home/'
    def form_valid(self, form):
        personal = form.save(commit=False)
        personal.user = self.request.user
        personal.save()
        return redirect('home')

class ContactAddressView(CreateView):
    form_class = ContactAddressForm
    template_name = 'main/contact_address.html'
    success_url = '/home/'
    def form_valid(self, form):
        Contact_address = form.save(commit = False)
        Contact_address.user = self.request.user
        Contact_address.save()
        return redirect('home')

class EmergencyContactView(CreateView):
    model = Emergency_contact
    form_class = EmergencyContactForm
    template_name = 'main/emergency_contact.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user # Link the user here
        return super().form_valid(form)
