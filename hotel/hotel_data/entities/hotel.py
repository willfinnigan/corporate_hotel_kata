from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from hotel.employee_data.entities.employee import Employee
from hotel.hotel_data.entities.room import Room, Booking


@dataclass
class Hotel:
    id: str
    name: str
    rooms: dict[int: Room] = field(default_factory=dict)

    def book_a_room(self, employee: Employee, room_type: str,  check_in: datetime, check_out: datetime) -> Booking:
        if check_out <= check_in:
            raise Exception('Checkout must be at least 1 day in the future')

        rooms = self.get_rooms_of_type(room_type)
        for room in rooms:
            if room.is_available(check_in, check_out):
                booking = Booking(room, check_in, check_out)
                room.bookings.append(booking)
                employee.bookings.append(booking)
                return booking

        raise Exception("No rooms available in desired timeframe")

    def create_or_update_room(self, room_type, room_num) -> Room:
        if room_num in self.rooms:
            room = self.rooms[room_num]
            room.room_type = room_type
            return room
        else:
            room = Room(room_type, room_num)
            self.rooms[room_num] = room
            return room

    def get_rooms(self) -> List[Room]:
        return list(self.rooms.values())

    def get_room_types(self) -> List[str]:
        return [room.room_type for room in self.get_rooms()]

    def get_rooms_of_type(self, room_type) -> List[Room]:
        rooms_of_type = []
        for room in self.rooms.values():
            if room.room_type == room_type:
                rooms_of_type.append(room)
        return rooms_of_type

    def number_of_rooms(self) -> int:
        return len(self.rooms)

    def get_all_bookings(self) -> List[Booking]:
        all_bookings = []
        for room in self.rooms.values():
            all_bookings += room.bookings
        return all_bookings

