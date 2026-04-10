from django.urls import path
from .views import RegisterView ,LoginView,HomeView,Personal

urlpatterns = [
    path('register/',RegisterView.as_view() , name='register'),
    path('logins/', LoginView.as_view() , name='logins'),
    path('',HomeView.as_view() , name="home"),
    path('personal',Personal.as_view() , name = "personal"),
]