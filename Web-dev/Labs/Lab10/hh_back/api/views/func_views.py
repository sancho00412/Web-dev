from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from api.models import Company, Vacancy

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        company_list = [company.to_json() for company in companies]
    
        return JsonResponse(company_list, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        company_name = data.get('name', '')
        company_description = data.get('description', '')
        company_city = data.get('city', '')
        company_address = data.get('address', '')
        company = Company.objects.create(name=company_name, description=company_description, city=company_city, address=company_address)
        return JsonResponse(company.to_json())


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    return JsonResponse(company.to_json())

def vacancy_by_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    vacancies = company.vacancies.all()
    vacancies_list = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_list, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancy_list = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_list, safe=False)

def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    return JsonResponse(vacancy.to_json())


def vacancy_top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancy_list = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_list, safe=False)

