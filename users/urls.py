from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('<int:user_id>/profile_edit/', views.profile_edit, name='profile_edit'),
] 
