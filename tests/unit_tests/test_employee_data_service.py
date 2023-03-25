import pytest

from hotel.employee_data.employee_data_service import EmployeeDataService


def test_can_create_a_company():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    assert employee_data_service.companies == {'company_1': company}

def test_can_retrieve_a_company():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    assert employee_data_service.get_company('company_1') == company

def test_can_create_an_employee():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    assert employee_data_service.employees == {'employee_1': employee}

def test_can_retrieve_an_employee():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    assert employee_data_service.get_employee('employee_1') == employee

def test_that_an_employee_that_does_not_exist_raises_an_exception():
    employee_data_service = EmployeeDataService()
    with pytest.raises(Exception):
        employee = employee_data_service.get_employee('does_not_exist')

def test_can_delete_an_employee():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    employee_data_service.delete_employee('employee_1')
    with pytest.raises(Exception):  # should raise exception because deleted
        employee = employee_data_service.get_employee('employee_1')

def test_employee_can_book_a_room_by_default():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    assert employee.is_allowed_to_book('double_room') == True

def test_employee_can_not_book_a_room_if_not_in_employee_booking_policy():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    employee.set_booking_policy(['single_room'])
    assert employee.is_allowed_to_book('double_room') == False

def test_employee_can_not_book_a_room_if_not_in_company_booking_policy():
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    company.set_booking_policy(['single_room'])
    assert employee.is_allowed_to_book('double_room') == False

