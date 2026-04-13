from django.urls import path
from .views import (RegisterView ,logout_view,HomeView,PersonalView,
                    ContactAddressView,EmergencyContactView ,
                    DinView, login_view,Add_CourseView,
                    TeacherRegisterView,
                    teachers,AssessmentsView)

urlpatterns = [
    path('register/',RegisterView.as_view() , name='register'),
    path('teacher_register/',TeacherRegisterView.as_view() , name='teacher_register'),
    path('logins/',login_view , name = 'logins'),
    path('',HomeView.as_view() , name="home"),
    path('personal/',PersonalView.as_view(), name = 'personal'),
    path('contactaddress/',ContactAddressView.as_view() , name= 'contactaddress'),
    path('emergencycontact/',EmergencyContactView.as_view(), name='emergencycontact' ),
    path('Din/', DinView.as_view() ,name= 'Din'),
    path('add_course/<int:pk>/', Add_CourseView.as_view(), name='add_course'),   
    path('logout/',logout_view,name='logout'),
    path('teachers/',teachers.as_view(), name='teachers'),
    path('assessment/<int:pk>/', AssessmentsView.as_view(), name='assessment'),


]