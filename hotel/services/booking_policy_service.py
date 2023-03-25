from typing import List

from hotel.employee_data.employee_data_service import EmployeeDataService


class BookingPolicyService:

    def __init__(self, employee_data_service: EmployeeDataService):
        self.employee_data_service = employee_data_service

    def setCompanyPolicy(self, company_id: str, allowed_room_types: List[str]):
        company = self.employee_data_service.get_company(company_id)
        company.set_booking_policy(allowed_room_types)

    def setEmployeePolicy(self, employeeId: str, allowed_room_types: List[str]):
        employee = self.employee_data_service.get_employee(employeeId)
        employee.set_booking_policy(allowed_room_types)

    def isBookingAllowed(self, employeeId: str, room_type: str):
        employee = self.employee_data_service.get_employee(employeeId)
        return employee.is_allowed_to_book(room_type)