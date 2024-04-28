from service import ControllerError


class Console:

    def __init__(self, game_controller):
        self.__game_controller = game_controller

    def start_game(self):
        game_in_progress = True
        while game_in_progress:
            yearly_report = self.__game_controller.get_yearly_report()
            print(yearly_report)
            waiting_for_input = True
            while waiting_for_input:
                try:
                    acres_to_buy_sell = int(input("Acres to buy/sell (+/-) -> "))
                    units_to_feed_population = int(input("Units to feed the population -> "))
                    acres_to_plant = int(input("Acres to plant -> "))
                    game_in_progress = self.__game_controller.new_turn(acres_to_buy_sell, units_to_feed_population, acres_to_plant)
                    print('-' * 34)
                    waiting_for_input = False
                except ValueError:
                    print("Value error: Make sure the inputs are valid positive integers.\n")
                except ControllerError as controller_error:
                    print(str(controller_error))

        final_report = self.__game_controller.get_yearly_report(final=True)
        print(final_report)
        if self.__game_controller.get_game_status() == "win":
            print("GAME OVER. The city is thriving, good job!")
        else:
            print("GAME OVER. You did not do very well.")