# Generated by Django 4.2.4 on 2023-08-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0004_alter_company_start_duration_skills_education_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Template 1', max_length=1000)),
                ('temp_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
