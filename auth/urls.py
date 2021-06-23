from django.urls import path
from .views import Login, Signup
from .userViews import UserList, UserDetail
from django.urls import path 
from .views import Login, Signup, Validation
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
    path('all-users/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),    
    path('validate/', Validation.as_view())
]