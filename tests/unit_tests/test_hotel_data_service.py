import pytest

from hotel.hotel_data.hotel_data_service import HotelDataService
from hotel.hotel_data.entities.hotel import Hotel


def test_can_add_a_hotel_to_hotel_repo():
    hotel_repo = HotelDataService()
    hotel_repo.add_hotel('hotel_1', 'A great hotel')

    assert hotel_repo.hotels == [Hotel('hotel_1', 'A great hotel')]

def test_can_find_hotel_by_id():
    hotel_repo = HotelDataService()
    hotel_repo.add_hotel('hotel_1', 'A great hotel')
    hotel = hotel_repo.find_hotel('hotel_1')
    assert hotel.name == 'A great hotel'

def test_find_hotel_raises_exception_if_no_id():
    hotel_repo = HotelDataService()
    with pytest.raises(Exception):
        hotel_repo.find_hotel('hotel_1')



