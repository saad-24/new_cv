from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('input_text/', views.input_text, name='input_text'),
    path('add_company/', views.add_company, name='add_company'),
    path('add_certification/', views.add_certification, name='add_certification'),
    path('add_education/', views.add_education, name='add_education'),
    path('add_skills/', views.add_skill, name='add_skills'),
]