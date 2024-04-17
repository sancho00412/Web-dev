from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)


@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(company.to_json(), safe=False)


def get_company_by_vacancy(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company does not exist'}, status=404)
    
    vacancies = Vacancy.objects.filter(company=company)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    
    return JsonResponse(vacancies_json, safe=False)


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)


@csrf_exempt
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json(), safe=False)


def vacancy_top_ten(request):
    if request.method == 'GET':
        vacancy_top_ten = Vacancy.objects.all().order_by('-salary')[:10]
        vacancy_top_ten_json = [v.to_json() for v in vacancy_top_ten]
        return JsonResponse(vacancy_top_ten_json, safe=False)
