from hotel.employee_data.employee_data_service import EmployeeDataService


class CompanyService:
    def __init__(self, employee_data_service: EmployeeDataService):
        self.employee_data_service = employee_data_service

    def add_employee(self, company_id: str, employee_id: str):
        if self.employee_data_service.does_company_exist(company_id) == False:
            self.employee_data_service.create_company(company_id)

        self.employee_data_service.create_employee(employee_id, company_id)

    def delete_employee(self, employee_id):
        self.employee_data_service.delete_employee(employee_id)

