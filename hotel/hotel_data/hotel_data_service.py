from dataclasses import dataclass, field
from typing import List

from hotel.hotel_data.entities.hotel import Hotel


@dataclass
class HotelDataService():
    hotels: List[Hotel] = field(default_factory=list)

    def add_hotel(self, hotel_id: str, hotel_name: str):
        hotel = Hotel(hotel_id, hotel_name)
        self.hotels.append(hotel)

    def find_hotel(self, hotel_id: str):
        for hotel in self.hotels:
            if hotel.id == hotel_id:
                return hotel
        raise Exception('Hotel not found')