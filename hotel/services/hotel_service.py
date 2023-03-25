from hotel.hotel_data.entities.hotel import Hotel
from hotel.hotel_data.hotel_data_service import HotelDataService


class HotelService:

    def __init__(self, hotel_data_service: HotelDataService):
        self.hotel_data_service = hotel_data_service

    def add_hotel(self, hotel_id: str, hotel_name: str):
        self.hotel_data_service.add_hotel(hotel_id, hotel_name)

    def find_hotel_by_id(self, hotel_id: str) -> Hotel:
        return self.hotel_data_service.find_hotel(hotel_id)

    def setRoom(self, hotel_id: str, num_room: int, room_type: str):
        hotel = self.find_hotel_by_id(hotel_id)
        hotel.create_or_update_room(room_type, num_room)

