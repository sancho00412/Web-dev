from django.urls import path

from api.views import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView, VacancyByCompanyAPIView, VacancyTopTenAPIView
# 

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),

    path('companies/<int:pk>/vacancies/', VacancyByCompanyAPIView.as_view()),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),

    path('vacancies/top_ten/', VacancyTopTenAPIView.as_view())
]