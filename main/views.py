from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView ,TemplateView, ListView ,DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Personal, Contact_address, Emergency_contact, Assessment ,CustomUserModel,Subject ,Classroom , Classroomstudent
from .forms import PersonalForm, ContactAddressForm, EmergencyContactForm, SubjectForm, AssessmentForm, TeacherCreationForm,StudentCreationForm, ClassroomForm ,Classroomstudentform

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
                return redirect('All_class')
            else:
                return redirect('home')
    return render(request, 'main/login.html')
@method_decorator(login_required(login_url='/logins/'), name='dispatch')
#student view 
class HomeView(DetailView):
    model = Personal
    context_object_name = 'personal'
    def get_object(self):
        try:
            return Personal.objects.get(user = self.request.user)
        except:
            pass
    template_name = 'main/home.html'
class Course_listVIew(ListView):
    model = Subject
    context_object_name = 'courses'
    template_name = 'main/student_subjects_list.html'
    def get_queryset(self):
        return Assessment.objects.filter(student = self.request.user)

class AssessmentListView(ListView):
    model = Assessment
    context_object_name = 'assessment'
    template_name = 'main/student_assessments_list.html'
    def get_queryset(self):
        course = Subject.objects.get(id = self.kwargs['id'])
        return Assessment.objects.get(course = course, student=self.request.user)
    
#teachers views 
class All_class(ListView):
    model = Classroom
    context_object_name = 'classes'
    template_name = 'main/section_list.html'
    def get_queryset(self):
        return Classroom.objects.filter(teacher=self.request.user)

class All_student(ListView):
    model = Classroomstudent
    context_object_name = 'students'
    template_name = 'main/student_list.html'
    def get_queryset(self):
        classes = Classroom.objects.get(id = self.kwargs['pk'])
        return Classroomstudent.objects.filter(classroom = classes)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_queryset()
        return context


class AssessmentsView(UpdateView):
    model = Assessment
    form_class = AssessmentForm
    context_object_name = 'assessment'
    template_name = 'main/assessment.html'
    success_url = 'teachers'


    '''
    def form_valid(self, form):
        form.save()
        return redirect('teachers')
    def get_object(self, queryset = ...):
        course = Course.objects.get(teacher=self.request.user)
        student = CustomUserModel.objects.get(id=self.kwargs['pk'])
        ass = Assessment.objects.get(course=course, student=student)
        return ass
    '''

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
#the super user or student din  views
class DinView(CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'main/Din.html'
    
    def form_valid(self, form):
        form.save()
        return redirect('/studadd/')

class Din_stud_add(CreateView):
    model = Classroomstudent
    form_class = Classroomstudentform
    template_name = 'main/student_add.html'
    success_url = 'subject_add'
    def form_valid(self, form):
        students = form.cleaned_data['students']
        try:
            for student in students:
                Classroomstudent.objects.create(student=student, classroom=form.cleaned_data['classroom'])
            return redirect('/subject_add/')
        except:
            pass
class Din_subject_add(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'main/subject_add.html'
    success_url = '/Din/'
    def form_valid(self, form):
        form.save()
        return redirect('/Din/')

def logout_view(request):
    logout(request)
    return redirect('logins')