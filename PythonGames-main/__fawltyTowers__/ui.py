from utils import Helper


class Console:

    def __init__(self, hotel_controller):
        self.__hotel_controller = hotel_controller

        self.__options = {
            "1": self.ui_create_room_reservation,
            "2": self.ui_delete_reservation,
            "3": self.ui_show_available_rooms,
            "4": self.ui_monthly_report,
            "5": self.ui_days_of_week_report
        }

    def show_menu(self):
        print("Choose from the available options below:")
        print("1. Create a room reservation.")
        print("2. Delete reservation.")
        print("3. Show available rooms.")
        print("4. Monthly report.")
        print("5. Days of week report.")
        print("0. Exit the app.")
        waiting_for_input = True
        while waiting_for_input:
            try:
                user_input = input(">> ")
                if user_input in self.__options:
                    self.__options[user_input]()
                elif user_input == "0":
                    waiting_for_input = False
                else:
                    print("Invalid option.")
            except ValueError as value_error:
                print(str(value_error))
            except Exception as exception:
                print(str(exception))

    def ui_create_room_reservation(self):
        family_name = input("Guest's family name: ").strip()
        room_type = input("Room type: ").strip()
        number_of_guests = int(input("Number of guests: ").strip())
        arrival_date = Helper.resolve_date(input("Arrival date: ").strip())
        departure_date = Helper.resolve_date(input("Departure date: ").strip())
        self.__hotel_controller.create_reservation(family_name, room_type, number_of_guests, arrival_date, departure_date)

    def ui_delete_reservation(self):
        uid = input("Reservation number: ").strip()
        self.__hotel_controller.delete_reservation(uid)

    def ui_show_available_rooms(self):
        date_interval = input("Time interval: ")
        start_date, end_date = map(Helper.resolve_date, date_interval.split('-'))
        for available_room in self.__hotel_controller.retrieve_available_rooms(start_date, end_date):
            print(str(available_room))

    def ui_monthly_report(self):
        for report in self.__hotel_controller.retrieve_monthly_report():
            print("Month: " + str(report["month"]) + ", reservation days: " + str(report["reservation_days"]))

    def ui_days_of_week_report(self):
        for report in self.__hotel_controller.retrieve_days_of_week_report():
            print("Day of week: " + str(report["day"]) + ", reserved rooms: " + str(report["reserved_rooms"]))