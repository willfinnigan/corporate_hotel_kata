import pytest

from hotel.hotel_data.hotel_data_service import HotelDataService
from hotel.services.hotel_service import HotelService


def test_hotel_service_throws_exception_if_hotel_already_exists():
    hotel_data_service = HotelDataService()
    hotel_service = HotelService(hotel_data_service)
    hotel_service.add_hotel('hotel_1', 'A great hotel')
    with pytest.raises(Exception):
        hotel_service.add_hotel('hotel_1', 'A great hotel')


def test_hotel_service_throws_exception_if_hotel_does_not_exist_when_setting_room():
    hotel_data_service = HotelDataService()
    hotel_service = HotelService(hotel_data_service)
    with pytest.raises(Exception):
        hotel_service.setRoom('does_not_exist', 1, 'double')

def test_hotel_service_find_hotel_returns_info_about_hotel_room_number():
    hotel_data_service = HotelDataService()
    hotel_service = HotelService(hotel_data_service)
    hotel_service.add_hotel('hotel_1', 'A great hotel')
    hotel_service.setRoom('hotel_1', 1, 'double')
    hotel = hotel_service.find_hotel_by_id('hotel_1')
    assert hotel.number_of_rooms() == 1