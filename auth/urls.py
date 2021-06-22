<<<<<<< HEAD
from django.urls import path
from .views import Login, Signup
from .userViews import UserList, UserDetail
=======
from django.urls import path 
from .views import Login, Signup, Validation
>>>>>>> 9c5119e0525d00c87325e8255de82d9c4a1f3e65
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
<<<<<<< HEAD
    path('all-users/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),    
=======
    path('validate/', Validation.as_view())
>>>>>>> 9c5119e0525d00c87325e8255de82d9c4a1f3e65
]