from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = ""
    description = models.CharField(max_length=128)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    picture = ""


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
