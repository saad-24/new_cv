from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# def view_own_cv(request):
#     user_cv = CV.objects.filter(user=request.user)
#     return render(request, 'cv/view_own_cv.html', {'user_cv': user_cv})

def home(request):
    saved_texts = user_data.objects.filter(user=request.user)
    saved_company = Company.objects.filter(user=request.user)
    return render(request, 'cv_app/home.html', {'saved_texts': saved_texts, 'saved_company':saved_company})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful registration
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'cv_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('success')
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'cv_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout.

@login_required
def input_text(request):
    if request.method == 'POST':
        entered_text = request.POST['entered_text']
        # user_data(text_data = entered_text).save()
        user_data.objects.create(text_data=entered_text, user=request.user)

    saved_texts = user_data.objects.filter(user=request.user)
    
    return render(request, 'cv_app/home.html', {'entered_text': entered_text, 'saved_texts': saved_texts})

@login_required
def add_company(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        Company.objects.create(name=company_name, user=request.user)
    saved_company = Company.objects.filter(user=request.user)
    # print(saved_company)


    return render(request, 'cv_app/home.html', {'company_name': company_name, 'saved_company': saved_company})


@login_required
def add_skill(request):
    if request.method == 'POST':
        skills = request.POST['skill']
        Skills.objects.create(name=skills, user=request.user)
    saved_skills = Skills.objects.filter(user=request.user)
    # print(saved_company)


    return render(request, 'cv_app/skills.html', {'skills': skills, 'saved_skills': saved_skills})

@login_required
def add_certification(request):
    if request.method == 'POST':
        certifications = request.POST['certification']
        certificate_issuer = request.POST['issuer']
        certificate_issue_date = request.POST['issue_date']

        Certifications.objects.create(name=certifications, issuer=certificate_issuer, issueDate=certificate_issue_date, user=request.user)

    saved_certifications = Certifications.objects.filter(user=request.user)
    # print(saved_company)


    return render(request, 'cv_app/certifications.html', {'certifications': certifications, 'certificate_issuer':certificate_issuer,'certificate_issue_date':certificate_issue_date,'saved_certifications': saved_certifications})


@login_required
def add_education(request):
    if request.method == 'POST':
        educations = request.POST['education']
        Education.objects.create(name=educations, user=request.user)
    saved_educations = Education.objects.filter(user=request.user)
    # print(saved_company)


    return render(request, 'cv_app/education.html', {'educations': educations, 'saved_educations': saved_educations})



