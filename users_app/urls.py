from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import UserProfile
from users_app import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', user_views.logout_site, name='logout'),
    path('<int:pk>/', UserProfile.as_view(), name='user-profle'),
]


