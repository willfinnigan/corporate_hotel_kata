from dataclasses import dataclass, field
from typing import Optional

from hotel.employee_data.entities.employee import Employee
from hotel.employee_data.entities.company import Company


@dataclass
class EmployeeDataService:
    companies: dict[str: Company] = field(default_factory=dict)
    employees: dict[str: Employee] = field(default_factory=dict)

    def get_employee(self, employee_id: str) -> Optional[Employee]:
        return self.employees.get(employee_id)

    def get_company(self, company_id: str) -> Company:
        return self.companies.get(company_id)

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
        employee = self.get_employee(employee_id)
        for i, booking in enumerate(employee.bookings):
            room = booking.room
            room.bookings.remove(booking)
        self.employees.pop(employee_id)

