from django.urls import path
from .views import RegisterView ,LoginView,HomeView,Personal,Contact_address,Emergency_contact

urlpatterns = [
    path('register/',RegisterView.as_view() , name='register'),
    path('logins/', LoginView.as_view() , name='logins'),
    path('',HomeView.as_view() , name="home"),
    path('personal/',Personal.as_view() , name = 'personal'),
    path('contactaddress/',Contact_address.as_view() , name= 'contactaddress'),
    path('emergencycontact/',Emergency_contact.as_view(), name='emergencycontact' ),
]