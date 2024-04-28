from service import ControllerError


class GameValidator:

    @staticmethod
    def validate_turn(situation, acres_to_buy_sell, units_to_feed_population, acres_to_plant):
        land_price = situation.get_land_price()
        grain_stocks = situation.get_grain_stocks()
        if acres_to_buy_sell * land_price > grain_stocks:
            raise ControllerError("You cannot buy more land than you have grain for.")
        acres_of_land = situation.get_acres_of_land()
        if acres_of_land + acres_to_buy_sell < 0:
            raise ControllerError("You cannot sell more land than you have.")
        acres_of_land = acres_of_land + acres_to_buy_sell
        grain_stocks = grain_stocks - acres_to_buy_sell * land_price
        if units_to_feed_population < 0:
            raise ControllerError("You cannot feed people a negative number of units.")
        if units_to_feed_population > grain_stocks:
            raise ControllerError("You cannot feed people with grain you do not have.")
        grain_stocks = grain_stocks - units_to_feed_population
        if acres_to_plant < 0:
            raise ControllerError("You cannot plant a negative number of acres.")
        if acres_to_plant > acres_of_land:
            raise ControllerError("You cannot plant more acres than you have.")
        if acres_to_plant > grain_stocks:
            raise ControllerError("You cannot plant grain that you do not have.")