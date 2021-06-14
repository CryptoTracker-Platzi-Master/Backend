from django.urls import path 
from .views import Login, Signup
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
]