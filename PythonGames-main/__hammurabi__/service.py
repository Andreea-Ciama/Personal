import random


class ControllerError(Exception):

    def __init__(self, message=None):
        if message is None:
            message = "Unknown error."
        self.__message = message

    def __str__(self):
        return "Controller ERROR: " + self.__message + "\n"


import random


class GameController:

    def __init__(self, game_situation, game_validator):
        self.__situation = game_situation
        self.__game_validator = game_validator

    def new_turn(self, acres_to_buy_sell, units_to_feed_population, acres_to_plant):
        # Validate the input from the player
        self.__game_validator.validate_turn(self.__situation, acres_to_buy_sell, units_to_feed_population, acres_to_plant)

        game_in_progress = True

        # Logic for buying/selling acres
        acres_of_land = self.__situation.get_acres_of_land()
        self.__situation.set_acres_of_land(acres_of_land + acres_to_buy_sell)
        grain_stocks = self.__situation.get_grain_stocks()
        land_price = self.__situation.get_land_price()
        self.__situation.set_grain_stocks(grain_stocks - acres_to_buy_sell * land_price)
        self.__situation.set_land_price(random.randint(15, 25))

        # Logic for feeding the population
        grain_stocks = self.__situation.get_grain_stocks()
        self.__situation.set_grain_stocks(grain_stocks - units_to_feed_population)
        city_population = self.__situation.get_city_population()
        starved_people = max(city_population - units_to_feed_population // 20, 0)
        if starved_people >= city_population // 2:
            game_in_progress = False
        new_people = random.randint(0, 10) if starved_people == 0 else 0
        self.__situation.set_starved_people(starved_people)
        self.__situation.set_new_people(new_people)
        self.__situation.set_city_population(city_population - starved_people + new_people)

        # Logic for harvesting
        grain_stocks = self.__situation.get_grain_stocks()
        units_harvested_per_acre = random.randint(1, 6)
        city_population = self.__situation.get_city_population()
        # Since every person can plant at most 10 acres, we're going to plant the minimum number of possible acres
        # considering the city population and the amount of acres to plant given by the player
        acres_to_plant = min(city_population * 10, acres_to_plant)
        self.__situation.set_units_harvested_per_acre(units_harvested_per_acre)
        self.__situation.set_grain_stocks(grain_stocks - acres_to_plant + acres_to_plant * units_harvested_per_acre)

        # Logic for rat infestation
        grain_stocks = self.__situation.get_grain_stocks()
        units_eaten = 0
        if random.random() < 0.2:
            units_eaten = int((grain_stocks * random.uniform(1, 10)) // 100)
        self.__situation.set_units_eaten(units_eaten)
        self.__situation.set_grain_stocks(grain_stocks - units_eaten)

        # Check whether we've reached the 5th year, otherwise keep going
        year = self.__situation.get_year() + 1
        if year == 5:
            game_in_progress = False
        self.__situation.set_year(year)

        return game_in_progress

    def get_game_status(self):
        city_population = self.__situation.get_city_population()
        acres_of_land = self.__situation.get_acres_of_land()
        if city_population > 100 and acres_of_land > 1000:
            return "win"
        else:
            return "lose"

    def get_yearly_report(self, final=False):
        return self.__situation.to_string(final)