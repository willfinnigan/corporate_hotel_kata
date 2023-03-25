import pytest
from hotel.employee_data.employee_data_service import EmployeeDataService
from hotel.services.company_service import CompanyService


def test_employee_service_throws_exception_if_trying_to_create_a_duplicate_employee():
    employee_data_service = EmployeeDataService()

    company_service = CompanyService(employee_data_service)
    company_service.add_employee('company_1', 'employee_1')

    with pytest.raises(Exception):
        company_service.add_employee('company_1', 'employee_1')




