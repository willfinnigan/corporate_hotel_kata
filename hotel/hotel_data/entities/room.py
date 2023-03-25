from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Booking:
    room: Room
    check_in: datetime
    check_out: datetime

@dataclass
class Room:
    room_type: str
    room_number: int
    bookings: List[Booking] = field(default_factory=list)

    def is_available(self, date_in, date_out) -> bool:
        for booking in self.bookings:
            if date_in >= booking.check_in and date_out <= booking.check_out:
                return False
        return True

