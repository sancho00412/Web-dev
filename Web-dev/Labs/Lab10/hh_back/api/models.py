from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Company Name')
    description = models.TextField(blank=True, verbose_name='Company Description')
    city = models.CharField(max_length=64, verbose_name='Company City')
    address = models.TextField(blank=True, verbose_name='Company Address')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "address": self.address,
        }
    

class Vacancy(models.Model):
    name = models.CharField(max_length=64, verbose_name='Vacancy Name')
    description = models.TextField(blank=True, verbose_name='Vacancy Description')
    salary = models.FloatField(default=0, verbose_name='Vacancy Salary')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies', verbose_name='Company')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.name
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "salary": self.salary,
            "company": self.company.name,
        }