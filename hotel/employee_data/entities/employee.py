from dataclasses import dataclass, field
from typing import List

from hotel.employee_data.entities.company import Company


@dataclass
class Employee:
    employee_id: str
    company: Company
    booking_policy: List[str] = field(default_factory=list)

    def set_booking_policy(self, booking_policy: List[str]):
        self.booking_policy = booking_policy

    def is_allowed_to_book(self, room_type: str):
        if len(self.booking_policy) == 0 and len(self.company.booking_policy) == 0:
            return True
        if room_type in self.booking_policy:
            return True
        if room_type in self.company.booking_policy:
            return True
        return False



