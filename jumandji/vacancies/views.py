from django.shortcuts import render, get_object_or_404
from django.views import View

from jumandji.settings import SITE_NAME

from .models import Company, Specialty, Vacancy


def my_render(request, html, data):
    data['SITE_NAME'] = SITE_NAME
    return render(request, html, data)


class MainView(View):
    def get(self, request):
        companies = Company.objects.filter()
        categories = Specialty.objects.filter()
        vacancy_count_for_company = []
        vacancy_count_for_category = []

        for c in companies:
            vacancy_count_for_company.append((c, Vacancy.objects.filter(company=c).count()))

        for c in categories:
            vacancy_count_for_category.append((c, Vacancy.objects.filter(specialty=c).count()))

        return my_render(request, 'vacancies/index.html', {'companies': vacancy_count_for_company,
                                                           'categories': vacancy_count_for_category
                                                           })


class VacancyView(View):
    def get(self, request, id=None, code=None):
        # /vacancies
        if not id and not code:
            path_to_file = 'vacancies/vacancies.html'
            context = {'vacancies': Vacancy.objects.filter(), 'specialty': 'Все вакансии'}
        # /vacancies/cat/code
        elif not id:
            vacancies = Vacancy.objects.filter(specialty__code=code)
            specialty = get_object_or_404(Specialty, code=code).title
            path_to_file = 'vacancies/vacancies.html'
            context = {'vacancies': vacancies, 'specialty': specialty}
        # /vacancies/id
        else:
            vacancy = get_object_or_404(Vacancy, id=id)
            path_to_file = 'vacancies/vacancy.html'
            context = {'vacancy': vacancy}

        return my_render(request, path_to_file, context)


class CompanyView(View):
    def get(self, request, id):
        company = get_object_or_404(Company, id=id)
        vacancies = Vacancy.objects.filter(company=company)

        return my_render(request, 'vacancies/company.html', {'company': company, 'vacancies': vacancies})
