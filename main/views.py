from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView ,TemplateView, ListView ,DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Personal, Contact_address, Emergency_contact, Course, Assessment ,CustomUserModel
from .forms import PersonalForm, ContactAddressForm, EmergencyContactForm, CourseForm, AssessmentForm, TeacherCreationForm,StudentCreationForm

# Create your views here.
class RegisterView(CreateView):
    form_class = StudentCreationForm
    template_name = 'main/register.html'
    success_url = '/logins/'

class TeacherRegisterView(CreateView):
    form_class = TeacherCreationForm
    template_name = 'main/teacher_register.html'
    success_url = '/logins/'

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user != None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('Din')
            elif request.user.is_teacher:
                return redirect('teachers')
            else:
                return redirect('home')
    return render(request, 'main/login.html')
@method_decorator(login_required(login_url='/logins/'), name='dispatch')
class HomeView(TemplateView):
    template_name = 'main/home.html'
class teachers(ListView):
    model = CustomUserModel
    context_object_name = 'students'
    template_name = 'main/teachers.html'

    def get_queryset(self):
        course = Course.objects.get(teacher=self.request.user)
        return course.student.all()
class AssessmentsView(UpdateView):
    model = Assessment
    form_class = AssessmentForm
    context_object_name = 'assessment'
    template_name = 'main/assessment.html'
    success_url = 'teachers'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_queryset(self):
        course = Course.objects.get(teacher=self.request.user)
        student = CustomUserModel.objects.get(id=self.kwargs['pk'])
        return Assessment.objects.filter(course=course, student=student)

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
class DinView(ListView):
    model = CustomUserModel
    context_object_name = 'students'
    template_name = 'main/Din.html'
    def get_queryset(self):
        return CustomUserModel.objects.filter(is_superuser=False)

class Add_CourseView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'main/add_course.html'
    def form_valid(self, form):
        course = form.save(commit=False)
        course.teacher = CustomUserModel.objects.get(subject=course.course_name)
        course.save()
        course.student.add(CustomUserModel.objects.get(id=self.kwargs['pk']))
        ass = Assessment(course=course, student=CustomUserModel.objects.get(id=self.kwargs['pk']))
        ass.save()
        return redirect('Din')

def logout_view(request):
    logout(request)
    return redirect('logins')