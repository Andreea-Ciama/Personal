from domain import *

from utils import Helper


class HotelRepository:

    def __init__(self, rooms_filename, reservations_filename):
        self.__rooms = []
        self.__reservations = []

        self.__rooms_filename = rooms_filename
        self.__reservations_filename = reservations_filename

        self.load_rooms_from_file()
        self.load_reservations_from_file()

    def add_reservation(self, reservation):
        self.__reservations.append(reservation)
        self.save_reservations_to_file()

    def remove_reservation(self, uid):
        reservation_index = self.get_reservation_index(uid)
        if reservation_index == -1:
            raise Exception("No reservation with the given number.")
        del self.__reservations[reservation_index]
        self.save_reservations_to_file()

    def get_rooms(self):
        return self.__rooms

    def get_reservations(self):
        return self.__reservations

    def get_available_rooms(self, arrival_date, departure_date, room_type=None):
        available_rooms = []
        for room in self.__rooms:
            room_number = room.get_number()
            if (room.get_type() == room_type or room_type is None) and self.not_reserved(room_number, arrival_date, departure_date):
                available_rooms.append(room)
        return available_rooms

    def get_monthly_report(self):
        report_list = []
        for month in range(1, 13):
            report = {"month": month, "reservation_days": self.get_reservation_days(month)}
            report_list.append(report)
        return sorted(report_list, key=lambda report: report["reservation_days"], reverse=True)

    def get_days_of_week_report(self):
        report_list = []
        for day in range(0, 7):
            report = {"day": Helper.get_formatted_day(day), "reserved_rooms": self.get_reserved_rooms(day)}
            report_list.append(report)
        return sorted(report_list, key=lambda report: report["reserved_rooms"], reverse=True)

    def get_reserved_rooms(self, weekday):
        reserved_rooms = 0
        for month in range(1, 13):
            for day in range(1, Helper.last_day_of_month(month) + 1):
                current_date = Helper.resolve_date(str(day) + "." + str(month))
                if current_date.weekday() == weekday:
                    reserved_rooms += len(self.__rooms) - len(self.get_available_rooms(current_date, current_date))
        return reserved_rooms

    def get_reservation_days(self, month):
        reservation_days = 0
        for reservation in self.__reservations:
            arrival_date = reservation.get_arrival_date()
            departure_date = reservation.get_departure_date()
            if arrival_date.month == month:
                if departure_date.month == month:
                    reservation_days += departure_date.day - arrival_date.day
                else:
                    reservation_days += Helper.last_day_of_month(month) - arrival_date.day
            if departure_date.month == month and arrival_date.month != month:
                reservation_days += departure_date.day
        return reservation_days

    def not_reserved(self, room_number, arrival_date, departure_date):
        for reservation in self.__reservations:
            reservation_room_number = reservation.get_room_number()
            if reservation_room_number == room_number:
                reservation_arrival_date = reservation.get_arrival_date()
                reservation_departure_date = reservation.get_departure_date()
                if (reservation_arrival_date <= arrival_date <= reservation_departure_date) or \
                        (reservation_arrival_date <= departure_date <= reservation_departure_date):
                    return False
        return True

    def get_reservation_index(self, uid):
        for reservation_index in range(len(self.__reservations)):
            reservation = self.__reservations[reservation_index]
            if reservation.get_uid() == uid:
                return reservation_index
        return -1

    def load_rooms_from_file(self):
        try:
            file = open(self.__rooms_filename, "r")
            line = file.readline().strip()
            while len(line) > 0:
                line = line.split(", ")
                room = Room(int(line[0]), line[1])
                self.__rooms.append(room)
                line = file.readline().strip()
            file.close()
        except IOError as io_error:
            print(str(io_error))

    def load_reservations_from_file(self):
        try:
            file = open(self.__reservations_filename, "r")
            line = file.readline().strip()
            while len(line) > 0:
                line = line.split(", ")
                reservation = Reservation(line[0], int(line[1]), line[2], int(line[3]),
                                          Helper.resolve_date(line[4]), Helper.resolve_date(line[5]))
                self.__reservations.append(reservation)
                line = file.readline().strip()
            file.close()
        except IOError as io_error:
            print(str(io_error))

    def save_reservations_to_file(self):
        file = open(self.__reservations_filename, "w")
        try:
            for reservation in self.__reservations:
                format_reservation = reservation.get_uid() + ", " + str(reservation.get_room_number()) + ", " + \
                                     reservation.get_family_name() + ", " + str(reservation.get_number_of_guests()) + ", " + \
                                     reservation.get_arrival_date().strftime("%d.%m") + ", " + reservation.get_departure_date().strftime("%d.%m") + "\n"
                file.write(format_reservation)
            file.close()
        except Exception as exception:
            print(str(exception))