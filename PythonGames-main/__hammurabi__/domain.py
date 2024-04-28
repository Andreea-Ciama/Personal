class Situation:

    def __init__(self):
        self.__year = 1
        self.__starved_people = 0
        self.__new_people = 0
        self.__city_population = 100
        self.__acres_of_land = 1000
        self.__units_harvested_per_acre = 3
        self.__units_eaten = 200
        self.__land_price = 20
        self.__grain_stocks = 2800

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_starved_people(self):
        return self.__starved_people

    def set_starved_people(self, starved_people):
        self.__starved_people = starved_people

    def get_new_people(self):
        return self.__new_people

    def set_new_people(self, new_people):
        self.__new_people = new_people

    def get_city_population(self):
        return self.__city_population

    def set_city_population(self, city_population):
        self.__city_population = city_population

    def get_acres_of_land(self):
        return self.__acres_of_land

    def set_acres_of_land(self, acres_of_land):
        self.__acres_of_land = acres_of_land

    def get_units_harvested_per_acre(self):
        return self.__units_harvested_per_acre

    def set_units_harvested_per_acre(self, units_harvested_per_acre):
        self.__units_harvested_per_acre = units_harvested_per_acre

    def get_units_eaten(self):
        return self.__units_eaten

    def set_units_eaten(self, units_eaten):
        self.__units_eaten = units_eaten

    def get_land_price(self):
        return self.__land_price

    def set_land_price(self, land_price):
        self.__land_price = land_price

    def get_grain_stocks(self):
        return self.__grain_stocks

    def set_grain_stocks(self, grain_stocks):
        self.__grain_stocks = grain_stocks

    def to_string(self, final):
        report_of_situation = "In year " + str(self.__year) + ", " + str(self.__starved_people) + " people starved.\n" + \
                              str(self.__new_people) + " people came to the city.\n" + \
                              "City population is " + str(self.__city_population) + ".\n" + \
                              "City owns " + str(self.__acres_of_land) + " acres of land.\n" + \
                              "Harvest was " + str(self.__units_harvested_per_acre) + " units per acre.\n" + \
                              "Rats ate " + str(self.__units_eaten) + " units.\n" + \
                              "Land price is " + str(self.__land_price) + " units per acre.\n" + \
                              ("\nGrain stocks are " + str(self.__grain_stocks) + " units.\n" if not final else "")
        return report_of_situation