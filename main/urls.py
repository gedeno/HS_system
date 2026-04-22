from django.urls import path
from .views import (RegisterView ,logout_view,HomeView,PersonalView,
                    ContactAddressView,EmergencyContactView ,
                    DinView, login_view,Din_subject_add, TeacherRegisterView,
                    All_class,AssessmentsView,Course_listVIew,
                    AssessmentListView,Din_stud_add
                    )

urlpatterns = [
    path('register/',RegisterView.as_view() , name='register'),
    path('teacher_register/',TeacherRegisterView.as_view() , name='teacher_register'),
    path('logins/',login_view , name = 'logins'),
    path('',HomeView.as_view() , name="home"),
    path('personal/',PersonalView.as_view(), name = 'personal'),
    path('contactaddress/',ContactAddressView.as_view() , name= 'contactaddress'),
    path('emergencycontact/',EmergencyContactView.as_view(), name='emergencycontact' ),
    path('Din/', DinView.as_view() ,name= 'Din'),
    path('studadd/', Din_stud_add.as_view() , name= 'studadd'),
    path('subject_add/', Din_subject_add.as_view(), name='subject_add'),   
    path('logout/',logout_view,name='logout'),
    path('All_class/',All_class.as_view(), name='All_class'),
    path('assessment/<int:pk>/', AssessmentsView.as_view(), name='assessment'),
    path('course_list/', Course_listVIew.as_view() , name = 'course_list'),
    path('assessment_list/<int:id>/',AssessmentListView.as_view(), name= 'assessment_list'),
    
    
]