import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "./module";
import {CompanyService} from "./company.service";
import {VacancyService} from "./vacancy.service";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
    title = 'hh-front';
    companies: Company[] = [];
    vacancies: Vacancy[] = [];
    company: string = "";

    constructor(private companyService: CompanyService, private vacancyService: VacancyService) {}
    ngOnInit() {
        this.companyService.getCompanies().subscribe((data) => {
            this.companies = data
        });
    }

    companySelect(id: number) {
        this.vacancyService.getVacanciesByCompany(id).subscribe((data) => {
            this.vacancies = data
            this.company = this.companies[id-1].name
        });
    }

}
