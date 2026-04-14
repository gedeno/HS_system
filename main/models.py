from django.db import models
from django.contrib.auth.models import AbstractUser,User, AbstractBaseUser

COURSE_CHOICES = (
    ('Mathematics', 'Mathematics'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('History', 'History'),
    ('Geography', 'Geography'),
    ('Literature', 'Literature'),
    ('Computer Science', 'Computer Science')
)
class CustomUserModel(AbstractUser):
    subject = models.CharField(max_length=40, null=True, blank=True, choices=COURSE_CHOICES)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

class Personal(models.Model):
    Choice_region  = (
        ('Afar','Afar'),
        ('Amhara','Amhara'),
        ('Beneshangul','Beneshangul'),
        ('Oromia','Oromia'),
        ('Somali','Somali'),
        ('Harari','Harari'),
        ('Tigray','Tigray'),
        ('Gambela','Gambela'),
        ('Sidama','Sidama'),
        ('SNNPR','SNNPR'),
        ('Addis Ababa','Addis Ababa'),
        ('Dire Dawa','Dire Dawa'),
    )
    profile_picture = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    grandfather_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    disability = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    region = models.CharField(max_length=200 , choices=Choice_region)
    marital_status = models.CharField(max_length=200)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='personal')

class Contact_address(models.Model):
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    zone = models.CharField(max_length=200)
    woreda = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    kebele = models.CharField(max_length=200)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='contact_address')

class Emergency_contact(models.Model):
    Full_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='emergency_contact')

class Course(models.Model):
    course_name = models.CharField(max_length=200, choices=COURSE_CHOICES)
    teacher = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE , related_name='courses')
    student = models.ManyToManyField(CustomUserModel)

class Assessment(models.Model):
    quiz1 = models.IntegerField(default=0)
    quiz2 = models.IntegerField(default=0)
    assignment1 = models.IntegerField(default=0)
    assignment2 = models.IntegerField(default=0)
    mid_exam = models.IntegerField(default=0)
    final_exam = models.IntegerField(default=0)
    course = models.OneToOneField(Course, on_delete=models.CASCADE , related_name='assessment')
    student = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='assessments')
