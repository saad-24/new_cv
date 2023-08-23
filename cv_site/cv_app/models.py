from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=200, null=False, default='ABC Solutions')
    designation = models.TextField(max_length=100, null=False, default='Engineer')
    start_duration = models.CharField(max_length=100,null=False, default='1')
    end_duration = models.CharField(max_length=100, null=False, default='Present')
    job_description = models.CharField(max_length=5000, null=False, default='Backend Engineer')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')


class user_data(models.Model):
    text_data = models.TextField(max_length=100)
    name = models.TextField(max_length=1000, null=False, default='Satoshi')
    email = models.EmailField(null=False, default='abc@example.com')
    github = models.CharField(max_length=200, default='None')
    linkedin = models.CharField(max_length=300, default='None')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

class Education(models.Model):
    institute = models.CharField(max_length=500, null=False, default='ABC Institute')

