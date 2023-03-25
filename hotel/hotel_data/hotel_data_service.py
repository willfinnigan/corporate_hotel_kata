from dataclasses import dataclass, field
from typing import List, Optional

from hotel.hotel_data.entities.hotel import Hotel


@dataclass
class HotelDataService():
    hotels: dict[str: Hotel] = field(default_factory=dict)

    def add_hotel(self, hotel_id: str, hotel_name: str) -> Hotel:
        hotel = Hotel(hotel_id, hotel_name)
        self.hotels[hotel_id] = hotel
        return hotel

    def find_hotel(self, hotel_id: str) -> Optional[Hotel]:
        return self.hotels.get(hotel_id)
