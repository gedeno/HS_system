from django.forms import ModelForm
from django import forms
from .models import Personal, Contact_address, Emergency_contact, Course, Assessment
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
