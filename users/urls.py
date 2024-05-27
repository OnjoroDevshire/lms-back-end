from django.urls import path
from .views import LoginView, LogoutView,UserProfileView,StudentRegisterView, TutorRegisterView

urlpatterns = [
    path('tutoregister/', TutorRegisterView.as_view(), name='register'),
    path('userprofile/', UserProfileView.as_view(), name='register'),
    path('studentregister/', StudentRegisterView.as_view(), name='register'),
    path('Login/', LoginView.as_view(), name='login'),
    path('Logout', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
