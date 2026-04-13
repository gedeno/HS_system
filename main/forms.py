from django.forms import ModelForm
from django import forms
from .models import Personal, Contact_address, Emergency_contact, Course, Assessment, CustomUserModel
from django.contrib.auth.forms import UserCreationForm

class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'subject', 'password1', 'password2']

    def save(self, commit = True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.subject = self.cleaned_data['subject']
        user.is_teacher = True
        if commit:
            user.save()
        return user
    
class StudentCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.is_student = True
        if commit:
            user.save()
        return user
class StudentCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'password1', 'password2']

    def save(self, commit = True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.is_student = True
        if commit:
            user.save()
        return user
    
class PersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        
class ContactAddressForm(ModelForm):
    class Meta:
        model = Contact_address
        fields = '__all__'
        exclude = ['user']
class EmergencyContactForm(ModelForm):
    class Meta:
        model = Emergency_contact
        fields = '__all__'
        exclude = ['user']
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['user']
class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'
        exclude = ['user']
