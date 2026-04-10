from django.urls import path
from .views import RegisterView ,LoginView,HomeView,PersonalView,ContactAddressView,EmergencyContactView

urlpatterns = [
    path('register/',RegisterView.as_view() , name='register'),
    path('logins/', LoginView.as_view() , name='logins'),
    path('',HomeView.as_view() , name="home"),
    path('personal/',PersonalView.as_view(), name = 'personal'),
    path('contactaddress/',ContactAddressView.as_view() , name= 'contactaddress'),
    path('emergencycontact/',EmergencyContactView.as_view(), name='emergencycontact' ),
]