
from django.http import Http404
from api.models import Company, Vacancy

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import CompanySerializer, VacancySerializer
from api.models import Company, Vacancy


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            raise Http404
        
    def get(self, request, pk=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk=None):
        company = self.get_object(pk)
        company.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class VacancyListAPIView(APIView):
    def get(self, request, pk=None):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\
        
class VacancyDetailAPIView(APIView):
    def get_object(self, pk):
        try: 
            return Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist as e:
            raise Http404
        
    def get(self, request, pk=None):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class VacancyByCompanyAPIView(APIView):
    def get(self, request, pk=None):
        try:
            company = Company.objects.get(id=pk)
            vacancies = company.vacancies.all()
            serializer = VacancySerializer(vacancies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            raise Http404
        
class VacancyTopTenAPIView(APIView):
    def get(self, request, pk=None):
        vacancies = Vacancy.objects.all().order_by("-salary")[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    