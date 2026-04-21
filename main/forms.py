from django.forms import ModelForm
from django import forms
from .models import Personal, Contact_address, Emergency_contact,  Assessment, CustomUserModel , Subject ,Classroom , Classroomstudent
from django.contrib.auth.forms import UserCreationForm

class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'subject', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': "Enter Usernafsdfsdfme..."
            }),
            'password1': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': "Enter Password..."
            }),
            'password2': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': "Confirm Password..."
            })
        }

    def save(self, commit = True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.subject = self.cleaned_data['subject']
        user.is_teacher = True
        if commit:
            user.save()
        return user
'''
class SectionsForm(ModelForm):
    teachers = forms.ModelChoiceField(queryset=CustomUserModel.objects.filter(is_teacher = True))
    students = forms.ModelMultipleChoiceField(
        queryset=CustomUserModel.objects.filter(is_student = True),
        widget=forms.SelectMultiple() # Default browser multi-select
    )
    class Meta:
        model = Sections
        fields = ['Grade','section','teachers', 'students']
'''

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username','grade', 'password1', 'password2']

    def save(self, commit = True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.grade = self.cleaned_data['grade']
        user.is_student = True
        if commit:
            user.save()
        return user
    
class ClassroomForm(ModelForm):
    teacher = forms.ModelMultipleChoiceField(
        queryset=CustomUserModel.objects.filter(is_teacher = True),
        #widget=forms.SelectMultiple() # Default browser multi-select
    )
    class Meta:
        model = Classroom
        fields = ['Grade','section','teacher']

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class Classroomstudentform(ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=CustomUserModel.objects.filter(is_student = True),
        widget=forms.SelectMultiple() # Default browser multi-select
    )
    class Meta:
        model = Classroomstudent
        fields = ['students' , 'classroom']


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

class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'
        exclude = ['user']
