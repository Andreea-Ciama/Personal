from datetime import date
import calendar
import random


class Helper:

    @staticmethod
    def resolve_date(date_string):
        day, month = map(int, date_string.split('.'))
        year = date.today().year
        return date(year, month, day)

    @staticmethod
    def generate_uid(objects):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while True:
            uid = ""
            for i in range(0, 4):
                uid += random.choice(digits)
            for item in objects:
                if item.get_uid() == uid:
                    continue
            return uid

    @staticmethod
    def int_in_range(a, b, x):
        return a <= x <= b

    @staticmethod
    def last_day_of_month(month):
        year = date.today().year
        month_range = calendar.monthrange(year, month)
        return month_range[1]

    @staticmethod
    def get_formatted_day(day):
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[day]