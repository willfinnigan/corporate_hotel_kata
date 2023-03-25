from datetime import datetime

import pytest

from hotel.employee_data.entities.company import Company
from hotel.employee_data.entities.employee import Employee
from hotel.hotel_data.entities.hotel import Hotel
from hotel.hotel_data.entities.room import Room, Booking
from hotel.hotel_data.hotel_data_service import HotelDataService

def create_test_employee() -> Employee:
    """This function is used by the tests below to create a mock employee"""
    company = Company('company_1')
    employee = Employee('employee_1', company)
    return employee


def test_can_add_a_hotel_to_hotel_repo():
    hotel_repo = HotelDataService()
    hotel = hotel_repo.add_hotel('hotel_1', 'A great hotel')
    assert hotel_repo.hotels == {'hotel_1': hotel}

def test_can_find_hotel_by_id():
    hotel_repo = HotelDataService()
    hotel_repo.add_hotel('hotel_1', 'A great hotel')
    hotel = hotel_repo.find_hotel('hotel_1')
    assert hotel.name == 'A great hotel'




def test_can_set_room_in_hotel():
    hotel = Hotel('hotel_1', 'A great hotel')
    room_1 = hotel.create_or_update_room('double', 1)
    assert hotel.rooms == {1: Room('double', 1)}

def test_book_a_room_in_hotel():
    hotel = Hotel('hotel_1', 'A great hotel')
    room_1 = hotel.create_or_update_room('double', 1)

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('12/19/22', '%m/%d/%y')

    employee = create_test_employee()

    booking = hotel.book_a_room(employee, 'double', check_in, check_out)

    assert hotel.get_all_bookings() == [Booking(room_1, check_in, check_out)]

def test_room_is_unavailable_once_booked():
    hotel = Hotel('hotel_2', 'A great hotel')
    room_1 = hotel.create_or_update_room('double', 1)

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('12/19/22', '%m/%d/%y')

    employee = create_test_employee()

    booking = hotel.book_a_room(employee, 'double', check_in, check_out)

    assert room_1.is_available(check_in, check_out) == False

    test_check_in = datetime.strptime('11/01/22', '%m/%d/%y')
    test_check_out = datetime.strptime('11/30/22', '%m/%d/%y')
    assert room_1.is_available(test_check_in, test_check_out) == False

def test_booking_check_in_date_and_check_out_date_on_same_day_raises_exception():
    # Check out date must be at least one day after the check in date.

    hotel = Hotel('hotel_2', 'A great hotel')
    room_1 = hotel.create_or_update_room('double', 1)

    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('10/19/22', '%m/%d/%y')
    employee = create_test_employee()

    with pytest.raises(Exception):
        booking = hotel.book_a_room(employee, 'double', check_in, check_out)



