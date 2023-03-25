from datetime import datetime

import pytest

from hotel.employee_data.employee_data_service import EmployeeDataService
from hotel.hotel_data.hotel_data_service import HotelDataService
from hotel.services.booking_service import BookingService


def create_test_booking_service():
    hotel_data_service = HotelDataService()
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')
    hotel = hotel_data_service.add_hotel('hotel_1', 'hotel')
    hotel.create_or_update_room('double', 1)
    booking_service = BookingService(hotel_data_service, employee_data_service)
    return booking_service


def test_booking_service_throw_exception_if_checkout_on_same_day_as_check_in():

    booking_service = create_test_booking_service()

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('10/19/22', '%m/%d/%y')

    with pytest.raises(Exception):
        booking = booking_service.book('employee_1', 'hotel_1', 'double', check_in, check_out)

def test_booking_service_throws_exception_if_hotel_does_not_exist():
    booking_service = create_test_booking_service()

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('10/25/22', '%m/%d/%y')

    with pytest.raises(Exception):
        booking = booking_service.book('employee_1', 'not_a_hotel', 'double', check_in, check_out)

def test_booking_service_throws_exception_if_room_type_does_not_exist():
    booking_service = create_test_booking_service()

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('10/25/22', '%m/%d/%y')

    with pytest.raises(Exception):
        booking = booking_service.book('employee_1', 'hotel_1', 'not_a_room_type', check_in, check_out)

def test_booking_not_allowed_if_no_rooms_available():
    booking_service = create_test_booking_service()

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('10/25/22', '%m/%d/%y')
    booking = booking_service.book('employee_1', 'hotel_1', 'double', check_in, check_out)

    with pytest.raises(Exception):
        check_in = datetime.strptime('10/20/22', '%m/%d/%y')
        check_out = datetime.strptime('10/24/22', '%m/%d/%y')
        booking = booking_service.book('employee_1', 'hotel_1', 'double', check_in, check_out)


