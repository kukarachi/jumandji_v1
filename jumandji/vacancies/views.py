from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class MainView(View):
    pass


class VacancyView(View):
    def get(self, request, id=None, code=None):
        if not id and not code:
            return HttpResponse('index')
        elif not id:
            return HttpResponse(f'specialization: {code}')
        else:
            return HttpResponse('id')


class CompanyView(View):
    def get(self, request, id):
        return render(request, 'vacancies/company.html')
