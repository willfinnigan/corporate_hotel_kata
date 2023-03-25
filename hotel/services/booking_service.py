from datetime import datetime
from hotel.employee_data.employee_data_service import EmployeeDataService
from hotel.hotel_data.entities.room import Booking
from hotel.hotel_data.hotel_data_service import HotelDataService


class BookingService:

    def __init__(self, hotel_data_service: HotelDataService, employee_data_service: EmployeeDataService):
        self.hotel_data_service = hotel_data_service
        self.employee_data_service = employee_data_service

    def book(self, employee_id: str, hotel_id: str, room_type: str, check_in: datetime, check_out: datetime) -> Booking:
        hotel = self.hotel_data_service.find_hotel(hotel_id)
        employee = self.employee_data_service.get_employee(employee_id)

        if employee.is_allowed_to_book(room_type) == False:
            raise Exception(f'Employee is not allowed to book this room.  (Employee id = {employee_id}, room_type = {room_type})')

        booking = hotel.book_a_room(employee, room_type, check_in, check_out)
        return booking

