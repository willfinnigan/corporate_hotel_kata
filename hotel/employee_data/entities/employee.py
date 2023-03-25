from dataclasses import dataclass, field
from typing import List

from hotel.employee_data.entities.company import Company
from hotel.hotel_data.entities.room import Booking


@dataclass
class Employee:
    employee_id: str
    company: Company
    bookings: List[Booking] = field(default_factory=list)
    booking_policy: List[str] = field(default_factory=list)


    def set_booking_policy(self, booking_policy: List[str]):
        self.booking_policy = list(set(booking_policy))

    def is_allowed_to_book(self, room_type: str):
        if len(self.booking_policy) == 0 and len(self.company.booking_policy) == 0:
            return True
        if room_type in self.booking_policy:
            return True
        if room_type in self.company.booking_policy:
            return True
        return False



