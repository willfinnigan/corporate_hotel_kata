from dataclasses import dataclass, field

from hotel.employee_data.entities.employee import Employee
from hotel.employee_data.entities.company import Company


@dataclass
class EmployeeDataService:
    companies: dict[str: Company] = field(default_factory=dict)
    employees: dict[str: Employee] = field(default_factory=dict)

    def get_employee(self, employee_id: str) -> Employee:
        employee = self.employees.get(employee_id)
        if employee is None:
            raise Exception(f'Employee does not exist (id={employee_id}')
        return employee

    def get_company(self, company_id: str) -> Company:
        company = self.companies.get(company_id)
        if company is None:
            raise Exception(f'Company does not exist (id={company_id}')
        return company

    def does_company_exist(self, company_id: str) -> bool:
        return company_id in self.companies

    def create_employee(self, employee_id: str, company_id: str) -> Employee:
        if company_id not in self.companies:
            raise Exception(f'Company does not exist (id={company_id})')

        company = self.companies[company_id]

        new_employee = Employee(employee_id, company)
        self.employees[employee_id] = new_employee
        return new_employee

    def create_company(self, company_id) -> Company:
        new_company = Company(company_id)
        self.companies[company_id] = new_company
        return new_company

    def delete_employee(self, employee_id: str):
        self.employees.pop(employee_id)
