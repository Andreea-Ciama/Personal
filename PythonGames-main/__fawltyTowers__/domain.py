# https://github.com/adrian-popa/fundamentals-of-programming/tree/master/tests/fawlty-towers/src
class Room:

    def __init__(self, number, type):
        self.__number = number
        self.__type = type

    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__type

    def __str__(self):
        return "Room " + str(self.__number) + ", type: " + self.__type


class Reservation:

    def __init__(self, uid, room_number, family_name, number_of_guests, arrival_date, departure_date):
        self.__uid = uid
        self.__room_number = room_number
        self.__family_name = family_name
        self.__number_of_guests = number_of_guests
        self.__arrival_date = arrival_date
        self.__departure_date = departure_date

    def get_uid(self):
        return self.__uid

    def get_room_number(self):
        return self.__room_number

    def get_family_name(self):
        return self.__family_name

    def get_number_of_guests(self):
        return self.__number_of_guests

    def get_arrival_date(self):
        return self.__arrival_date

    def get_departure_date(self):
        return self.__departure_date
