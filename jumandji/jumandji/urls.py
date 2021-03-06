"""jumandji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from vacancies.views import CompanyView, MainView, VacancyView

# regex path for combining vacancies/cat/code and vacancies/id
# re_path(r'^vacancies/(?P<id>\d+)?/?(cat/(?P<code>\w+))?/$', VacancyView.as_view(), name='vacancies')


urlpatterns = [
    path('', MainView.as_view()),
    path('companies/<int:id>/', CompanyView.as_view(), name='companies'),
    path('vacancies/cat/<str:code>/', VacancyView.as_view(), name='vacancies/cat'),
    path('vacancies/<int:id>/', VacancyView.as_view(), name='vacancies/id'),
    path('vacancies/', VacancyView.as_view()),
]
