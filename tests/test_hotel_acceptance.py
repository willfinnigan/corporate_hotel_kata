from datetime import datetime

from hotel.employee_data.employee_data_service import EmployeeDataService
from hotel.services.booking_policy_service import BookingPolicyService
from hotel.services.booking_service import BookingService
from hotel.hotel_data.entities.room import Booking
from hotel.hotel_data.hotel_data_service import HotelDataService
from hotel.services.company_service import CompanyService
from hotel.services.hotel_service import HotelService

def test_hotel_manager_can_define_rooms_in_hotel():
    """Acceptance test from the view of the hotel manager"""

    hotel_data_service = HotelDataService()
    hotel_service = HotelService(hotel_data_service)

    hotel_service.add_hotel('hotel_1', 'A great hotel')
    hotel_service.setRoom('hotel_1', 1, 'double')
    hotel_service.setRoom('hotel_1', 2, 'double')
    hotel_service.setRoom('hotel_1', 3, 'single')
    hotel_service.setRoom('hotel_1', 4, 'triple')
    hotel_service.setRoom('hotel_1', 5, 'double')

    hotel_service.add_hotel('hotel_2', 'An awful hotel')
    hotel_service.setRoom('hotel_2', 1, 'single')
    hotel_service.setRoom('hotel_2', 2, 'single')
    hotel_service.setRoom('hotel_2', 3, 'single')
    hotel_service.setRoom('hotel_2', 4, 'single')
    hotel_service.setRoom('hotel_2', 5, 'double')

    hotel_1 = hotel_service.find_hotel_by_id('hotel_1')
    assert len(hotel_1.rooms) == 5

    hotel_2 = hotel_service.find_hotel_by_id('hotel_2')
    assert len(hotel_2.get_rooms_of_type('single')) == 4


def test_company_admin_can_create_a_new_employee_and_set_employee_booking_policy():
    """Acceptance test from the view of the company admin"""

    employee_data_service = EmployeeDataService()
    
    company_service = CompanyService(employee_data_service)
    company_service.add_employee('company_1', 'employee_1')

    booking_policy_service = BookingPolicyService(employee_data_service)
    booking_policy_service.setCompanyPolicy('company_1', ['double'])
    booking_policy_service.setEmployeePolicy('employee_1', ['single'])

    assert booking_policy_service.isBookingAllowed('employee_1', 'single') == True
    assert booking_policy_service.isBookingAllowed('employee_1', 'double') == True
    assert booking_policy_service.isBookingAllowed('employee_1', 'triple') == False


def test_that_employee_can_book_a_room():
    """Acceptance test from the view of a employee"""

    hotel_data_service = HotelDataService()
    employee_data_service = EmployeeDataService()
    company = employee_data_service.create_company('company_1')
    employee = employee_data_service.create_employee('employee_1', 'company_1')

    hotel_service = HotelService(hotel_data_service)
    hotel_service.add_hotel('hotel_1', 'A great hotel')
    hotel_service.setRoom('hotel_1', 1, 'double')

    booking_service = BookingService(hotel_data_service, employee_data_service)
    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('12/19/22', '%m/%d/%y')
    booking = booking_service.book('employee_1', 'hotel_1', 'double', check_in, check_out)

    assert isinstance(booking, Booking)


def test_deleted_employee_has_all_bookings_deleted():
    hotel_data_service = HotelDataService()
    employee_data_service = EmployeeDataService()

    company_service = CompanyService(employee_data_service)
    company_service.add_employee('company_1', 'employee_1')


    hotel_service = HotelService(hotel_data_service)
    hotel_service.add_hotel('hotel_1', 'A great hotel')
    hotel_service.setRoom('hotel_1', 1, 'double')

    booking_service = BookingService(hotel_data_service, employee_data_service)
    check_in = datetime.strptime('10/19/22', '%m/%d/%y')
    check_out = datetime.strptime('12/19/22', '%m/%d/%y')
    booking = booking_service.book('employee_1', 'hotel_1', 'double', check_in, check_out)

    company_service.delete_employee('employee_1')

    hotel = hotel_service.find_hotel_by_id('hotel_1')
    bookings = hotel.get_all_bookings()
    assert len(bookings) == 0












