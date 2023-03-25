from dataclasses import dataclass, field
from typing import List


@dataclass
class Company:
    company_id: str
    booking_policy: List[str] = field(default_factory=list)

    def set_booking_policy(self, booking_policy):
        self.booking_policy = list(set(booking_policy))